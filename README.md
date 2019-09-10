# DDD-Flask-Demo

Demo of the Flask Application Framework for Python

## The Setup

Virtual Environment setup

```bash
C:\project_folder> virtualenv venv
```

Activate virtual environment

```bash
C:\project_folder> venv\Scripts\activate
```

Install Flask

```bash
pip install flask
```

Basic Template

```py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Flask Demo</h1>"


@app.route("/about")
def about():
    return "<h1>About Us</h1>"
```

Setting Environmental Variarbles

```bash
# mac/linux
export FLASK_APP = file_name.py

# windows
set FLASK_APP = file_name.py

# windows powershell
$env:FLASK_APP="file_name.py"
```

Run the application

```bash
C:\project_folder> flask run
```
