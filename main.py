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
    <body>
        <h1>Signup</h1>
        <form action="/welcome" method="post">
            <label for="Username">Username:</label>
            <input id="Username" type="text" name="Username" />
            <br>
            <label for="Password">Password:</label>
            <input id="Password" type="text" name="Password" />
            <br>
            <label for="VerifyPassword">Verify Password:</label>
            <input id="VerifyPassword" type="text" name="VerifyPassword" />
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

@app.route("/welcome", methods = ["GET", "POST"])
def welcome():
    #Username = request.args.get('Username')
    Username = request.form['Username']
    return '<h1> Welcome, ' + Username + '! </h1>'

app.run()