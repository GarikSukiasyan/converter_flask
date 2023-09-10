import os
import os.path
# https://github.com/miguelgrinberg/Flask-SocketIO/tree/main/example
from app import app, socketio
from flask import jsonify
from threading import Thread
from flask import render_template
from flask_socketio import SocketIO, emit, join_room
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
            progress, stat, file_id, fileName = "progress", "stat", "file_id", "fileName"  #xt.info_thr()
            data = {'progress': progress, 'download': stat, 'file_id': file_id, 'nameFile': fileName}
            return jsonify(data)
    else:
        data = {'progress': 0, 'download': 'False', 'file_id': file_id, 'nameFile': 'None'}
        return jsonify(data)




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

        list_file_process.remove(file_id)
        print(list_file_process)
        self.status = True

    def start_thr(self, file_id):
        Thread(target=self.procc_ffmpeg, args=(file_id, )).start()

    def info_thr(self, stat=None):
        if stat:
            self.progress = stat
        else:
            return self.progress, self.status, self.file_id, self.fileName








# @socketio.on('connect', namespace='/test')
# def test_connect():
#     emit('update_data', {'progress': 0})
#     simulate_progress()





def simulate_progress(file_id):
    """Он не может остановиться почему то"""
    xt = ffm()

    # print(list_file_process)
    xt.start_thr(file_id)  # Запускаем конверт

    progress = 0
    while progress < 95:
        socketio.sleep(1)  # Имитация задержки в выполнении
        progress_tx, stat, file_id2, fileName = xt.info_thr()
        data = {'progress': int(progress_tx), 'download': stat, 'file_id': file_id2, 'nameFile': fileName}
        progress = int(progress_tx)
        # print(file_id)
        # print(file_id, progress_tx)
        socketio.emit('update_data', data, namespace="/test", room=file_id)


@socketio.on("connect", namespace='/test')
def test_connect():
    print("connect")
    # socketio.start_background_task(target=simulate_progress)


@socketio.on('join', namespace='/test')
def on_join(room):
    join_room(room)
    print('Присоединено к комнате:', room)
    list_file_process.append(room)

    while list_file_process.index(room) != 0:
        print('Ждем очереди : ' + str(room))
        socketio.sleep(1)
    socketio.start_background_task(target=simulate_progress(room))


@socketio.on("disconnect", namespace='/test')
def test_disconnect():
    print("disconnect")


@socketio.on('count_update', namespace='/test')
def handle_count_update(data):
    count = data['count']
    emit('count_update', {'count': count}, broadcast=True)