from app import app, all_user_key
from flask import render_template


@app.route('/output/<path:id>')
def output(id):
    print(all_user_key)
    # Ваш код обработки перехода по URL с переменной id
    return render_template("output.html")