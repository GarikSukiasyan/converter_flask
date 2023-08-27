from app import app
from flask import render_template
# from config import all_user_key


@app.route('/output/<path:id>')
def output(id):
    # print(all_user_key)
    # Ваш код обработки перехода по URL с переменной id
    return render_template("output.html")