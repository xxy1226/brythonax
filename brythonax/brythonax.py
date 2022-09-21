from flask import render_template, Blueprint, url_for, send_from_directory, request
import os

bp = Blueprint('brythonax', __name__)

@bp.route('/', method = ['GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

@bp.route('/demo')
def demo():
    return render_template('demo.html')

@bp.route('/leetcode')
def leetcode():
    return render_template('LeetCode.html')

@bp.route('/unleetcode')
def leetcode():
    return render_template('unLeetCode.html')

@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')