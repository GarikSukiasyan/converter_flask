import random
import threading
import time
from app import app
from flask import render_template
from flask import Flask, jsonify, request


@app.route('/')
def home():
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