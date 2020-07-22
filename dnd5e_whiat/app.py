""" Main app/routing file"""

from flask import Flask, render_template
from .models import DB, Character, add_character

def create_app():
    """ Create and configures an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html')
    
    @app.route('/add_characters')
    def add_ch():
        DB.drop_all() #Always Reset First
        DB.create_all()
        add_character()
        return 'Characters added!'
    
    @app.route('/view_characters')
    def view_ch():
        characters = Character.query.all()
        return '\n'.join([str(character) for character in characters])
        
    return app