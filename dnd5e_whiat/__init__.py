#!user/bin/env python
"""
Entry point for the Flask application.
"""

from .app import create_app

APP = create_app()
