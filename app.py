from flask import Flask, render_template, url_for, request
from forms import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'aBcDeFgHiJkLmNoP123'

# index/login
@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    form_username = request.form.getlist('username_input')
    form_password = request.form.getlist('password_input')
    print(f'username: {form_username} password: {form_password}')
  
  return render_template('login.html')

# register
@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  return render_template("register.html", form=form)

# about
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)