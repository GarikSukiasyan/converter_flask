from flask_socketio import SocketIO
from flask import Flask
# pip install gevent-websocket
# pip install eventlet
app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet') #, cors_allowed_origins="*")

# Список id пользователей (ссылок) в очереди
all_user_key = []

# Импорт обработчика
from .views import views
from .views import views_other
from .views import views_documents
from .views import views_videos
from .views import views_images
from .views import views_output