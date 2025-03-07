import sys
import os

# Set the project home directory
project_home = u'/home/aisis/myFirstProject'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import your Flask app. Ensure that 'app' is the Flask instance in app.py.
from app import app as application
