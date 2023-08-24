from app import app
from flask import render_template


@app.route('/images')
def images():
    return render_template("images.html")
