from flask import Flask

app = Flask(__name__)

# Импорт обработчика
from .views import views
from .views import views_other
from .views import views_documents
from .views import views_videos
from .views import views_images
from .views import views_output