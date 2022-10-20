from flask import render_template, Blueprint, url_for, send_from_directory, request, make_response
# import brythonax.settings as settings
import os

bp = Blueprint('brythonax', __name__)

@bp.route('/')
@bp.route('/<lan>/home')
def home(len='en'):
    if request.method == 'GET':
        return render_template('index.html')

@bp.route('/demo')
@bp.route('/<lan>/demo')
def demo(lan='en'):
    if lan == 'cn':
        return render_template('cn/demo.html')
    return render_template('en/demo.html')

@bp.route('/demo')
@bp.route('/<lan>/demo')
def doc(lan='en'):
    if lan == 'cn':
        return render_template('cn/docs/intro.html')
    return render_template('en/docs/intro.html')

@bp.route('/leetcode')
def leetcode():
    return render_template('LeetCode.html')

@bp.route('/unleetcode')
def unleetcode():
    return render_template('unLeetCode.html')

@bp.route('/test')
@bp.route('/test/<name>')
def test(name=None):
    return render_template('test.html', name=name)

@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')