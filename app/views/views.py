import time
import random
import threading
from app import app, all_user_key
from flask import render_template
from flask import jsonify, request


@app.route('/')
def home():
    print(all_user_key)
    # Возвращаем шаблон страницы и передаем данные из базы
    return render_template("home.html")


# https://learn.javascript.ru/xmlhttprequest
# Маршрут для обработки GET-запроса
@app.route("/data", methods=["GET"])
def get_data():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)


@app.route("/progress", methods=["GET"])
def get_progress():
    data = {'progress': random.randint(0, 99)}
    return jsonify(data)