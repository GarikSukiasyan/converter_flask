import os
import os.path
import time

from app import app, socketio
from flask import jsonify
from threading import Thread
from flask import render_template
from flask_socketio import SocketIO, emit
from ffmpeg_progress_yield import FfmpegProgress
# https://pypi.org/project/ffmpeg-progress-yield/

list_file_process = [] # Добавь очередь








@app.route('/output/<path:file_id>')
def output(file_id):
    if os.path.isdir(f"app/static/output/{file_id}/"):
        # print("Папка существует.")

        # Проверяем наличие файлов
        file_list = os.listdir(f"app/static/output/{file_id}/")
        if len(file_list) == 2:
            json_data = {'progress': 100, 'download': True, 'file_id': file_id, 'nameFile': file_list[1]}
            return render_template("output.html", json_data=json_data)

        elif len(file_list) == 1:  # Если один файл

            list_file_process.append(file_id)

            # xt.start_thr(file_id)  # Запускаем конверт

            json_data = {'progress': 0, 'download': False, 'file_id': file_id, 'nameFile': 'None'}
            return render_template("output.html", json_data=json_data)
    else:
        # print("Папка не существует.")
        return render_template('other/404.html'), 404




@app.route("/ffmpeg_status/<file_id>", methods=["GET"])
def ffmpeg_status(file_id):
    if os.path.isdir(f"app/static/output/{file_id}/"):
        if file_id not in list_file_process:
            file_list = os.listdir(f"app/static/output/{file_id}/")
            if len(file_list) == 2:
                data = {'progress': 100, 'download': 'True', 'file_id': file_id, 'nameFile': file_list[1]}
                return jsonify(data)
            else:
                data = {'progress': 0, 'download': 'False', 'file_id': file_id, 'nameFile': 'None'}
                return jsonify(data)
        else:
            progress, stat, file_id, fileName = xt.info_thr()
            data = {'progress': progress, 'download': stat, 'file_id': file_id, 'nameFile': fileName}
            return jsonify(data)
    else:
        data = {'progress': 0, 'download': 'False', 'file_id': file_id, 'nameFile': 'None'}
        return jsonify(data)



# @socketio.on('connect')
# def handle_connect():
#     print('Клиент подключился')


# https://man.archlinux.org/man/python-flask-socketio.1.en
# Обработчик для обработки подключения к сокету
# @socketio.on('connect', namespace='/test')
# def test_connect():
#     print('Client connected')


# @socketio.on('connect', namespace='/test')
# def test_connect():
    # while True:
    # emit('update_data', {'data': 'Connected'})
    # json_data = {'progress': 0, 'download': False, 'file_id': 'self.file_id', 'nameFile': "self.fileName"}
    # emit('update_data', json_data)
    # update_count(json_data)


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('update_data', {'progress': 0})
    simulate_progress()

def simulate_progress():
    progress = 0
    while progress < 100:
        time.sleep(0.3)  # Имитация задержки в выполнении
        print('push')
        # progress, stat, file_id, fileName = xt.info_thr()
        data = {'progress': int(progress), 'download': 'stat', 'file_id': 'file_id', 'nameFile': 'fileName'}
        progress += 10
        # print(progress)
        emit('update_data', data)


@socketio.on('count_update', namespace='/test')
def handle_count_update(data):
    count = data['count']
    emit('count_update', {'count': count}, broadcast=True)



def update_count(json_data):
    emit('count_update', json_data, namespace='/test', broadcast=True)

# Пример вызова функции update_count из кода сервера
# count = 10
# update_count(count)


@app.route('/update')
def update():
    # Отправляем сообщение "Hello" на клиента событием "updatedata"
    socketio.emit('updatedata', 'Hello', broadcast=True)
    return 'Update Sent'


class ffm():
    def __init__(self):
        self.progress = 0
        self.status = False
        self.file_id = ''
        self.fileName = ''

    def procc_ffmpeg(self, file_id):

        file_list = os.listdir(f"app/static/output/{file_id}/")

        cmd = [
            "ffmpeg",
            "-i", f"app/static/output/{file_id}/{file_list[0]}",
            "-c:a", "copy",
            f"app/static/output/{file_id}/output.mp4",
        ]

        ff = FfmpegProgress(cmd)
        for progress in ff.run_command_with_progress():
            self.progress = progress
            # json_data = {'progress': progress, 'download': False, 'file_id': self.file_id, 'nameFile': self.fileName}
            # emit('update_data', json_data)
            # update_count(json_data)
            print(f"{progress}/100")

        list_file_process.remove(file_id)
        self.status = True

    def start_thr(self, file_id):
        # print('1')
        Thread(target=self.procc_ffmpeg, args=(file_id, )).start()

    def info_thr(self, stat=None):
        if stat:
            self.progress = stat
        else:
            return self.progress, self.status, self.file_id, self.fileName




xt = ffm()


