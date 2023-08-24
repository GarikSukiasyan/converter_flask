import os
import random
from app import app
from flask import request, flash, render_template, redirect, url_for
from werkzeug.utils import secure_filename


# папка для сохранения загруженных файлов
UPLOAD_FOLDER = 'app/static/uploadFile/'
# расширения файлов, которые разрешено загружать
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'gif'}
# конфигурируем Загрузку файлов
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 МБ


def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Функция загрузки файлов
# https://www.youtube.com/watch?v=pPSZpCVRbvQ
@app.route('/videos', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        format_video = request.form.get('my_select')
        print(format_video)

        if 'file' not in request.files:
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            len_files = len(os.listdir("app/static/uploadFile/"))
            filename = int(len_files) + int(1)
            filename = str(file.filename) + "_" + str(filename) + str(".mp4")

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('home'), 302)

    return render_template("videos.html")