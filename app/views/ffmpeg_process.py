from threading import Thread
import random
import time
import random
import threading
from app import app, all_user_key
from flask import render_template
from flask import jsonify, request


from flask import jsonify, request
from ffmpeg_progress_yield import FfmpegProgress
# https://pypi.org/project/ffmpeg-progress-yield/






def procc_ffmpeg(path, file_id):
    cmd = [
        "ffmpeg",
        "-i", f"app/static/uploadFile/{path}",
        "-c:a", "copy",
        f"output_{random.randint(0, 99)}.mp4",
    ]

    ff = FfmpegProgress(cmd)
    for progress in ff.run_command_with_progress():
        print(f"{progress}/100")


def start_thr(path, file_id):
    print('1')
    Thread(target=start_thr, args=(path, file_id, )).start()



def info_thr():
    pass





@app.route("/ffmpeg_start", methods=["GET"])
def ffmpeg_start():
    data = {'all_num_mb': 0, 'all_num_file': 0}
    return jsonify(data)



@app.route("/ffmpeg_status", methods=["GET"])
def ffmpeg_status():
    data = {'all_num_mb': 0, 'all_num_file': 0}
    return jsonify(data)





