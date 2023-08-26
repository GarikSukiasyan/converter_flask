import threading
import time

from app import app
from flask import render_template

from app import app, socketio


@app.route('/')
def home():
    # Возвращаем шаблон страницы и передаем данные из базы
    return render_template("home.html")


# Функция для выполнения подсчета
def count_to_million():
    for i in range(10):
        time.sleep(1.0)
        # Отправляем текущее значение на фронтенд
        socketio.emit('count_update', {'count': i}, namespace='/test')


# Обработчик для обработки подключения к сокету
@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')
    # Запускаем фоновый поток для выполнения подсчета
    threading.Thread(target=count_to_million).start()

# Отправляем статический HTML-файл для отображения подсчета
@app.route('/test')
def test():
    return render_template('test.html')

