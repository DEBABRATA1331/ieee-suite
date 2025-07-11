# excom_dashboard/__init__.py

from flask import Blueprint

# Initialize Blueprint
excom_bp = Blueprint(
    'excom',
    __name__,
    template_folder='templates',
    static_folder='static'  # optional if using custom static files for this module
)

# Import routes to register them with the blueprint
from . import routes

