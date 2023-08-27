from app import app

# Дебаг FLASK
CFG_DEBUG_FLASK = True

# Секретный ключ
app.secret_key = 'aamffeogrbrjbwr09vj131'

# Список id пользователей (ссылок) в очереди
all_user_key = []