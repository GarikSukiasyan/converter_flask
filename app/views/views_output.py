import os
import os.path

from app import app, all_user_key
from flask import render_template, request, send_from_directory
from threading import Thread
import random
from app import app
from flask import render_template
from flask import flash, render_template, redirect, make_response
from flask import jsonify
from ffmpeg_progress_yield import FfmpegProgress
# https://pypi.org/project/ffmpeg-progress-yield/

list_file = []



@app.route('/output/<path:id>')
def output(id):
    # print(all_user_key)
    # Ваш код обработки перехода по URL с переменной id
    return render_template("output.html")


class ffm():
    def __init__(self):
        self.progress = 0
        self.status = False

    def procc_ffmpeg(self, path, file_id):
        # os.mkdir(f"app/static/output/{file_id}")

        cmd = [
            "ffmpeg",
            "-i", f"app/static/uploadFile/{path}",
            "-c:a", "copy",
            f"app/static/output/{file_id}/output.mp4",
        ]

        ff = FfmpegProgress(cmd)
        for progress in ff.run_command_with_progress():
            self.progress = progress
            # print(f"{progress}/100")

        list_file.remove(file_id)
        self.status = True

    def start_thr(self, path, file_id):
        # print('1')
        Thread(target=self.procc_ffmpeg, args=(path, file_id, )).start()

    def info_thr(self, stat=None):
        if stat:
            self.progress = stat
        else:
            return self.progress, self.status



xt = ffm()

@app.route("/ffmpeg_start", methods=["GET"])
def ffmpeg_start():
    file_id = request.cookies.get('id')
    path = request.cookies.get('outputFileName')
    # print(file_id)

    if file_id:
        if file_id not in list_file and file_id != "0":

            if os.path.isdir(f"app/static/output/{file_id}"):
                # Папка существует
                data = {'progress': 100, 'download': True}

                return jsonify(data)
            else:
                # Папка не существует

                os.mkdir(f"app/static/output/{file_id}")

                list_file.append(file_id)
                # print('start ', file_id)

                xt.procc_ffmpeg(path, file_id)
                data = {'progress': 0, 'download': False}

                return jsonify(data)

        else:
            progress, stat = xt.info_thr()
            if stat == False:
                data = {'progress': progress, 'download': False}
                return jsonify(data)
            elif stat == True:
                # Передаем что бы создал кнопку для скачивания файла и больше не присылал запросы
                data = {'progress': 100, 'download': True}

                response = make_response(jsonify(data))
                response.set_cookie("id", "0", max_age=60 * 60 * 24 * 365 * 2)
                return response

                # return jsonify(data)


    stat = xt.info_thr()
    data = {'progress': stat, 'download': True}
    return jsonify(data)


@app.route("/ffmpeg_status", methods=["GET"])
def ffmpeg_status():
    data = {'all_num_mb': 0, 'all_num_file': 0}
    return jsonify(data)




@app.route('/output/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory='pdf', filename=filename)