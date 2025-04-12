from flask import render_template
from main import app  # Correct import of the Flask app


@app.route('/about')
def about():
    return render_template('about.html')  # Using the right function
