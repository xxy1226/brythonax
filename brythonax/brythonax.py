from flask import render_template, Blueprint, url_for, send_from_directory, request, make_response
# import brythonax.settings as settings
import os

bp = Blueprint('brythonax', __name__)

@bp.route('/setcookie')
def set_cookie():
    resp = make_response(f"The Cookie has been set")
    resp.set_cookie("Lan", "en")
    return resp

@bp.route('/getcookie')
def getcookie():
    lan = request.cookies.get('Lan', None)
    return f"Language: {lan}"

@bp.route('/')
@bp.route('/home')
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