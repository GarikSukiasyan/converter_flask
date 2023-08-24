from app import app
from flask import render_template


@app.route('/documents')
def documents():
    return render_template("documents.html")