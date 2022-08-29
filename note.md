# 创建虚拟环境
`py -m venv .venv`
.venv/Scripts/activate.ps1

# 安装 Flask 和 Gunicorn
`pip install flask`

# 生成文件结构
`mkdir brythonax`
`mkdir brythonax\static`
`mkdir brythonax\templates`

# 安装 Brython
`pip install brython`
`cd brythonax\templates`
`py -m brython install`
`cd ../..`

# 生成需求库列表
`pip freeze >> requirements.txt`

# 创建 Heroku Procfile 文件
`echo 'web: gunicorn "bryhonax:create_app()"' >> Procfile`

# 上传至 Heroku
1. 登录 (Heroku)[https://id.heroku.com/login]
2. New -> Create new app
3. 根据指示操作
   1. `heroku login`
   2. `git init`
   3. `heroku git:remote -a brythonax`
   4. `git add requirements.txt Procfile note.md brythonax`
   5. `git commit -m first_commit`