import os
import random
from app import app, all_user_key
from flask import flash, render_template, redirect, make_response
from werkzeug.utils import secure_filename
from flask import jsonify, request

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

        format_video = request.form.get('my_select')
        # print(format_video)

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
            response = make_response(redirect(f'/output/{file_id}'))
            all_user_key.append(file_id)

            oldFileName = secure_filename(file.filename)
            # print(filename)

            len_files = len(os.listdir("app/static/uploadFile/"))
            filename = int(len_files) + int(1)
            filename = str(file.filename) + "_" + str(filename) + str(".mp4")
            # print(filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            response.set_cookie("id", file_id, max_age=60*60*24*365*2)
            response.set_cookie("progressBar", "0", max_age=60 * 60 * 24 * 365 * 2)
            response.set_cookie("inputFileName", oldFileName, max_age=60 * 60 * 24 * 365 * 2)
            response.set_cookie("outputFileName", filename, max_age=60 * 60 * 24 * 365 * 2)

            # start_thr(filename, file_id)

            return response

    response = make_response(render_template("videos.html"))
    response.set_cookie("id", "0", max_age=60 * 60 * 24 * 365 * 2)
    return response