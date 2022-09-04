from flask import render_template, Blueprint, url_for, send_from_directory
import os

bp = Blueprint('brythonax', __name__)

@bp.route('/')
@bp.route('/home')
def home():
    return render_template('index.html')

@bp.route('/demo')
def demo():
    return render_template('demo.html')

@bp.route('/leetcode')
def leetcode():
    return render_template('LeetCode.html')

@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')