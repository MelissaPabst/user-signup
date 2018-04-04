from flask import Flask, request, redirect, render_template
import cgi
import os
#import jinja2

#sets path, could be removed with importing render_template from flask, not importing jinja2
#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

#allows for debugging
app = Flask(__name__)
app.config['DEBUG'] = True



#creates route for signup form

@app.route("/")
def display_form():
    return render_template('signup.html')


#generic functions for validations. can be applied to fields as necessary.

def is_proper_length(x):
    if len(x) >= 3 and len(x) <21:
        return True
    else:
        return False

def is_not_empty(x):
    if len(x) > 0:
        return True
    else:
        return False

def space_in_x(x):
    if " " in x:
        return True
    else:
        return False

def at_in_email(x):
    if x.count('@') == 1:
        return True
    else:
        return False

def period_in_email(x):
    if x.count('.') == 1:
        return True
    else:
        return False



#creates route for validation

@app.route("/", methods=['GET', 'POST'])
def verify_signup():

    #creates variables from form inputs

    username = request.form["Username"]
    password = request.form["Password"]
    password2 = request.form["VerifyPassword"]
    email = request.form["email"]

    #creates empty strings for error messages

    username_error = ''
    password_error = ''
    password2_error = ''
    email_error = ''

    #validations for username

    if not is_not_empty(username):
        username_error = "Username required."
        #username = ''
    elif not is_proper_length(username):
        username_error = "Username must be between 3-20 characters."
        #username = ''
    elif space_in_x(username):
        username_error = "Username must not contain spaces."
        #username = ''
    else:
        username = username
    
    #validations for passwords

    if not is_not_empty(password):
        password_error = "Password is required."
        password = ''
        password2 = password2
    elif not is_proper_length(password):
        password_error = "Password must be between 3-20 characters."
        password = ''
        #password2 = ''
    elif space_in_x(password):
        password_error = "Password must not contain spaces."
        password = ''
        #password2 = ''
        
    if not is_not_empty(password2):
        password2_error = "Password is requried."
        #password = ''
        password2 = ''
    elif not is_proper_length(password2):
        password2_error = "Password must be between 3-20 characters."
        #password = ''
        password2 = ''
    elif space_in_x(password2):
        password2_error = "Password must not contain spaces."
        #password = ''
        password2 = ''

    if not password_error and not password2_error:
        if password != password2:
            password_error = "Passwords must match."
            password2_error = "Passwords must match."
            password = ''
            password2 = ''
       

    #validations for email
    if is_not_empty(email):
        if space_in_x(email):
            email_error = "Email must not contain spaces."
        if not is_proper_length(email):
            email_error = "Must be between 3-20 characters."
        if not period_in_email(email):
            email_error = 'Email must contain a "."'
        if not at_in_email(email):
            email_error = 'Email must contain a "@" sign.'
    else:
        email_error = ''
        email = email
    
    #redirect to welcome page if all fields are okay

    if not username_error and not password_error and not password2_error and not email_error: 
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error=username_error, username=username, password_error=password_error, password=password, password2_error=password2_error, email_error=email_error, email=email)

#creates route for welcome page   

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    #username = request.form['Username'] for methods=['POST']
    
    return render_template('welcome.html', username=username)

if __name__ == "__main__":
    app.run()