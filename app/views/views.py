from app import app
from flask import render_template



@app.route('/')
def home():
    # Возвращаем шаблон страницы и передаем данные из базы
    return render_template("home.html")