# waitress_server.py
from waitress import serve
from app import app
import os

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))  # Default to 5000
    print(f"Serving on http://127.0.0.1:{port} using Waitress...")
    serve(app, host='0.0.0.0', port=port)
