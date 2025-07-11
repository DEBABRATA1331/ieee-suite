from flask import Blueprint, render_template, request, session
import pandas as pd

feedback_bp = Blueprint('feedback', __name__, template_folder='templates')

@feedback_bp.route('/feedback', methods=['GET', 'POST'])
def feedback_analyzer():
    feedback_data = None
    avg_score = None
    total_score_count = 0
    optional_feedbacks = []

    # Ensure user is logged in
    username = session.get('user', 'guest')
    role = session.get('role', 'member')

    if request.method == 'POST':
        uploaded_file = request.files['csv']
        if uploaded_file and uploaded_file.filename.endswith('.csv'):
            try:
                df = pd.read_csv(uploaded_file)

                # Filter columns like 5., 6., etc. for score calculation
                score_columns = [
                    col for col in df.columns if col.startswith(("5.", "6.", "7.", "8.", "9.", "10.", "11."))
                ]

                numeric_scores = df[score_columns].apply(pd.to_numeric, errors='coerce')
                total_score_count = numeric_scores.count().sum()
                total_score_sum = numeric_scores.sum().sum()

                if total_score_count > 0:
                    avg_score = round(total_score_sum / total_score_count, 2)

                # Optional feedback
                if '1. Name' in df.columns and '12. Open Feedback (Optional)' in df.columns:
                    feedback_data = df.head().to_html(classes="table table-striped", index=False)
                    for _, row in df[['1. Name', '12. Open Feedback (Optional)']].dropna().iterrows():
                        comment = row['12. Open Feedback (Optional)'].strip()
                        if comment.lower() not in ['.', 'no answer', '']:
                            optional_feedbacks.append({
                                'name': row['1. Name'],
                                'comment': comment
                            })

            except Exception as e:
                print("Error processing CSV:", e)

    return render_template(
        'feedback.html',
        user=username,
        role=role,
        feedback_data=feedback_data,
        avg_score=avg_score,
        total_score_count=total_score_count,
        optional_feedbacks=optional_feedbacks
    )
