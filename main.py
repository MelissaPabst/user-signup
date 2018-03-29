from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

signup_form = """
<!doctype html>
<html>
<head>
    <style>
        .error{color:red;}
    </style>
    <body>
        <h1>Signup</h1>
        <form action="/welcome" method="post">
            <label for="Username">Username:</label>
            <input id="Username" type="text" name="Username" />
            <br>
            <label for="Password">Password:</label>
            <input id="Password" type="password" name="Password" />
            <br>
            <label for="VerifyPassword">Verify Password:</label>
            <input id="VerifyPassword" type="password" name="VerifyPassword" />
            <br>
            <label for="email">Email (not required):</label>
            <input id="email" type="text" name="email" />
            <br>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return signup_form

@app.route("/", methods=["GET","POST"])
def verify_signup():

    username = request.form["Username"]
    password = request.form["Password"]
    password2 = request.form["VerifyPassword"]
    email = request.form["email"]

    username_error = ''
    password_error = ''
    email_error = ''

    if len(username) == 0:
        username_error = "Not a valid Username."
    elif ' ' in username:
        username_error = "Not a valid Username."
    elif len(username) > 20:
        username_error = "Not a valid Username."
    elif len(username) < 3:
        username_error = "Not a valid Username."

    if len(password) == 0:
        password_error = "Not a valid Password."
    elif ' ' in username:
        password_error = "Not a valid Password."
    elif len(password) > 20:
        password_error = "Not a valid Password."
    elif len(password) < 3:
        password_error = "Not a valid Password."

    if password != password2:
        password2_error = "Passwords do not match."

    if not username_error and not password_error and not password2_error: 
        return redirect('/welcome')
    else:
    

@app.route("/welcome", methods = ["GET", "POST"])
def welcome():
    #Username = request.args.get('Username')
    Username = request.form['Username']
    return '<h1> Welcome, ' + Username + '! </h1>'

app.run()