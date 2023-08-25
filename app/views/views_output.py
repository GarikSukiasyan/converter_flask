from app import app
from flask import render_template


@app.route('/output/<path:id>')
def output(id):
    print(id)
    # Ваш код обработки перехода по URL с переменной id
    return render_template("output.html")