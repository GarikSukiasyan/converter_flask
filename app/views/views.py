import time
import random
import threading
from app import app, all_user_key
from flask import render_template
from flask import jsonify, request


@app.route('/')
def home():
    # print(all_user_key)
    # Возвращаем шаблон страницы и передаем данные из базы
    json_data = {'progress': 0, 'download': False, 'file_id': 'file_name1', 'nameFile': 'None'}
    return render_template("home.html", json_data=json_data)


# https://learn.javascript.ru/xmlhttprequest
# Маршрут для обработки GET-запроса
@app.route("/info", methods=["GET"])
def get_data():
    data = {'all_num_mb': 0, 'all_num_file': 0}
    return jsonify(data)


