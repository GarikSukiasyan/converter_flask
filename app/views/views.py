from app import app
from flask import render_template



@app.route('/')
def home():
    # Возвращаем шаблон страницы и передаем данные из базы
    return render_template("home.html")

@app.route('/videos')
def videos():
    return render_template("videos.html")

@app.route('/documents')
def documents():
    return render_template("documents.html")

@app.route('/images')
def images():
    return render_template("images.html")
