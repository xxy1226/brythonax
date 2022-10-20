from flask import render_template, Blueprint, url_for, send_from_directory, request, session
import brythonax.settings as settings
import os

bp = Blueprint('brythonax', __name__)

def set_session_lan(lan = "en"):
    if not (lan not in settings.LAN and 'lan' in session.keys()):
        session['lan'] = lan
        
def remove_session():
    for key in session.keys():
        session.pop(key)

@bp.route('/')
@bp.route('/<lan>/home')
def home():
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
def test():
    return render_template('test.html')

@bp.route('/language', methods = ['GET'])
def language():
    set_session_lan(request.args.get('lan'))
    return print_session()

@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')