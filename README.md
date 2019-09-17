# DDD-Flask-Demo

Demo of the Flask Micro Web Framework

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
# import Flask class
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# Routes
# use of @ decorator to add functionality the Flask instance route method
# It allows the dev to only write functionality that will be displayed

# stacked decorators
# both routes handled by the same function
@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Flask Demo</h1>"


@app.route("/about")
def about():
    return "<h1>About Us</h1>"
```

Setting Environmental Variarbles

```bash
# The enviroment variable will point to the file that holds the Flask application

# mac/linux
export FLASK_APP = file_name.py

# windows
set FLASK_APP = file_name.py

# windows powershell
$env:FLASK_APP="file_name.py"
```

Run the application

```bash
# Setting the environtment variable allows us to simply run the app as follows
C:\project_folder> flask run
```

Run the application without having to restart the server, set the environment variable FLASK_DEBUG = 1

```bash
# mac/linux
export FLASK_DEBUG = 1

# windows
set FLASK_DEBUG = 1

# windows powershell
$env:FLASK_DEBUG=1
```

Run the app without using environmental variables

```bash
# This condition is only true if this script is run directly
# as the name of the module would be __main__
# However using the env vars allows for additional debugging

if __name__ == '__main__':
  app.run(debug=True)
```

## Templates

Flask will by default look for HTML and related files in the templates folder.

In the app file, import render template from flask.

js/css files go into the static folder if neccessary.

```bash
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return render_template('index.html')


@app.route("/about")
def about():
    return "<h1>About Us</h1>"

if __name__ == '__main__':
  app.run(debug=True)
```

### Jinja2


### Template inheritance

Create parent template that the others will inherit from.
Block is a section that the child templates can override
