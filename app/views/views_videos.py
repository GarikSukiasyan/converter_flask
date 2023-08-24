from app import app
from flask import render_template


@app.route('/videos')
def videos():
    return render_template("videos.html")
