import dataiku
from flask import send_from_directory
import os

# --- MODIFIED PART ---

# Get the directory where this app.py file lives
# This will be: .../geologwannabe-app/
webapp_dir = os.path.dirname(__file__)

# Go up two levels to get to the plugin's root directory
# from .../geologwannabe-app/  to  .../geologwannabe-plugin/
plugin_root = os.path.dirname(os.path.dirname(webapp_dir))

# Now, build the full path to your 'build' directory from the plugin root
build_dir = os.path.join(plugin_root, 'resources', 'react-app')

# --- END MODIFIED PART ---


# This is the main entry point, it serves the index.html
# This code does not need to change.
@app.route('/')
def index():
    return send_from_directory(build_dir, 'index.html')

# This route serves all the other static files (JS, CSS, etc.)
# This code does not need to change.
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(build_dir, path)