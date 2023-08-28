import os
from app import app
from flask import send_from_directory, render_template




# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('other/404.html'), 404


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, '../static'), 'favicon.ico', mimetype='favicon.ico')

