from flask import Flask, render_template, url_for, request
from forms import RegistrationForm

app = Flask(__name__)

# secret key neccessary for form submission, encryption, etc
app.config['SECRET_KEY'] = 'aBcDeFgHiJkLmNoP123'

# index/login
@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def home():
  # code to verify form submitted properly
  # for demo purposes only
  if request.method == 'POST':
    form_username = request.form.getlist('username_input')
    form_password = request.form.getlist('password_input')
    print(f'username: {form_username} password: {form_password}')
  
  return render_template('login.html')

# register
@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm(request.form)

  # code to verify form submitted properly
  # for demo purposes only
  if request.method == 'POST':
    form_username = form.username.data
    form_email = form.email.data
    form_password = form.password.data
    print(f'username: {form_username} email: {form_email} password: {form_password}')
  
  return render_template("register.html", form=form)

# about
@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)