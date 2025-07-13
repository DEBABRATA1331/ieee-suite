from flask import Flask, render_template, request, redirect, url_for, session
from notice_generator.routes import notice_bp
from feedback_analyzer.routes import feedback_bp
from excom_dashboard.routes import excom_bp
from datetime import datetime
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "fallback-secret")

#Secure session config for HTTPS (Render)
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_SAMESITE='None'
)

#Prevent caching to fix redirect/stale page issues
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

# Register blueprints
app.register_blueprint(notice_bp)
app.register_blueprint(feedback_bp)
app.register_blueprint(excom_bp)

# Load users safely from users.json
def load_users():
    try:
        with open('users.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        # Debug print statements
        print(f"[DEBUG] Trying login for username: {username}")
        print(f"[DEBUG] Password entered: {password}")
        print(f"[DEBUG] User found: {username in users}")

        if username in users:
            hash_check = check_password_hash(users[username]['password'], password)
            print(f"[DEBUG] Password hash check result: {hash_check}")

            if hash_check:
                session['user'] = username
                session['role'] = users[username].get('role', 'member')
                print(f"[DEBUG] Session set: {session}")
                return redirect(url_for('dashboard'))

        return render_template('login.html', error="Invalid username or password.")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    print(f"[DEBUG] Session contents at dashboard: {dict(session)}")
    if 'user' not in session:
        print("[DEBUG] No user in session, redirecting to login.")
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
