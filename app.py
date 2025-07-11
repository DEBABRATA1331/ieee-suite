from flask import Flask, render_template, request, redirect, url_for, session
from notice_generator.routes import notice_bp
from feedback_analyzer.routes import feedback_bp
from excom_dashboard.routes import excom_bp
from datetime import datetime
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret")  # secure from .env

# Register Blueprints
app.register_blueprint(notice_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(excom_bp)

# Load users from users.json
def load_users():
    with open('users.json') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username]['password'], password):
            session['user'] = username
            session['role'] = users[username].get('role', 'member')
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid username or password.")
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template(
        'dashboard.html',
        user=session['user'],
        role=session.get('role', 'member'),
        current_year=datetime.now().year,
        current_date=datetime.now().strftime('%A, %B %d, %Y')
    )

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False)
