import os
import os.path
from app import app
from flask import jsonify
from threading import Thread
from flask import render_template
from ffmpeg_progress_yield import FfmpegProgress
# https://pypi.org/project/ffmpeg-progress-yield/

list_file_process = []




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
            # print(f"{progress}/100")

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

            xt.start_thr(file_id)  # Запускаем конверт

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
