"""
Entry point for the PestSentry API.
Initializes and configures the Flask application,
setting up necessary system paths for module imports
Starts the Flask development server.
"""

#Import necessary functions and modules
from app.app import create_app
from app.config import DevelopmentConfig, PACKAGE_ROOT
import sys
import os
PACKAGE_ROOT = os.path.join(os.pardir)
sys.path.append(PACKAGE_ROOT)

# Define the root directory for models and add it to system path
MODELS_ROOT = os.path.join(PACKAGE_ROOT, "models")
sys.path.append(MODELS_ROOT)

# Create the app instance with the development configuration
application = create_app(config_object=DevelopmentConfig)

# Run the application on all available IP addresses
if __name__ == '__main__':
	application.run(host='0.0.0.0')
