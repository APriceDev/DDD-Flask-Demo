from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def home():
  form_email = request.form.getlist('email_input')
  form_password = request.form.getlist('password_input')
  print(f'email: {form_email} password: {form_password}')
  return render_template('login.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)