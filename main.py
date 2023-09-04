from config import app, socketio
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

print("http://127.0.0.1:5000/")

if __name__ == "__main__":

    # Локальный доступ
    # app.run(debug=True)
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)