from flask import render_template, Blueprint, url_for

bp = Blueprint('brythonax', __name__)

@bp.route('/')
@bp.route('/home')
def home():
    return render_template('index.html')