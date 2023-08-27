from flask import Flask

app = Flask(__name__)

# Список id пользователей (ссылок) в очереди
all_user_key = []

# Импорт обработчика
from .views import views
from .views import views_other
from .views import views_documents
from .views import views_videos
from .views import views_images
from .views import views_output