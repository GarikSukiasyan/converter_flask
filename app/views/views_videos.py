import os
import random
from app import app, all_user_key
from flask import flash, render_template, redirect
from flask import request

# папка для сохранения загруженных файлов
UPLOAD_FOLDER = 'app/static/uploadFile/'
# расширения файлов, которые разрешено загружать
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'gif'}
# конфигурируем Загрузку файлов
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 МБ


def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Функция загрузки файлов
# https://www.youtube.com/watch?v=pPSZpCVRbvQ
@app.route('/videos', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            file_id = ''
            for i in range(24):
                file_id += random.choice(chars)
            all_user_key.append(file_id)

            os.mkdir(f"app/static/output/{file_id}")

            file_name = file.filename
            file_name = file_name.split(".")

            file.save(os.path.join(f"app/static/output/{file_id}", f"input.{file_name[1]}"))

            return redirect(f'/output/{file_id}')

    return render_template("videos.html")