import os
import random
import subprocess

from app import app
from flask import request, flash, render_template, redirect, url_for, make_response
from werkzeug.utils import secure_filename


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
            response = make_response(redirect('/output/iasd231sd/'))

            oldFileName = secure_filename(file.filename)
            # print(filename)

            len_files = len(os.listdir("app/static/uploadFile/"))
            filename = int(len_files) + int(1)
            filename = str(file.filename) + "_" + str(filename) + str(".mp4")

            # print(filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            response.set_cookie("id", "iasd231sd", max_age=60*60*24*365*2)
            response.set_cookie("progressBar", "0", max_age=60 * 60 * 24 * 365 * 2)
            response.set_cookie("inputFileName", oldFileName, max_age=60 * 60 * 24 * 365 * 2)
            response.set_cookie("outputFileName", filename, max_age=60 * 60 * 24 * 365 * 2)

            # https://pypi.org/project/ffmpeg-progress-yield/
            # ffmpeg -i input.mkv -vcodec copy -acodec copy output.mov
            subprocess.call([
                "ffmpeg",
                "-i", f"app/static/uploadFile/{filename}",
                "-c:a", "copy",
                f"app/static/output/{filename}.avi"])

            return response

    return render_template("videos.html")