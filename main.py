from config import app
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

print("http://127.0.0.1:5000/")

if __name__ == "__main__":

    # Локальный доступ
    app.run(debug=True)
