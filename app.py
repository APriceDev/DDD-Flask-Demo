from flask import Flask, render_template, url_for

app = Flask(__name__)

data = [ 
  {
    'title': 'BPI',
    'id': 1
  },
  {
    'title': 'Foo',
    'id': 2
  }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('index.html', data=data)


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)