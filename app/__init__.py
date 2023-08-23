from flask import Flask

app = Flask(__name__)


# Импорт обработчика
from .views import views
from .views import views_other