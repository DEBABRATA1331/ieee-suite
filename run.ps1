# PowerShell script to launch the IEEE ExCom Suite

Clear-Host
Write-Host "`n=== Launching IEEE VSSUT ExCom Dashboard Suite ===`n" -ForegroundColor Cyan

Set-Location "D:\ieee-suite"

# Create virtual environment if not exists
if (!(Test-Path "./venv")) {
    Write-Host "`nCreating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "`nActivating environment & installing dependencies..." -ForegroundColor Green
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install flask python-docx pandas pywin32 werkzeug

# Set environment variables
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"

# Run the Flask app
Write-Host "`nStarting Flask development server..." -ForegroundColor Green
flask run
