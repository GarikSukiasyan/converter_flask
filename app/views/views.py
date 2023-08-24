from app import app
from flask import render_template




@app.route('/')
def home():
    # Возвращаем шаблон страницы и передаем данные из базы
    return render_template("home.html")


@app.route('/output/<path:id>')
def output(id):
    # Ваш код обработки перехода по URL с переменной id
    return 'Переход по URL: output/{}'.format(id)
