#import items
from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
import re
#*****************************

# Using Jinja2 for Templates
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True) 

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/user_signup')
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

#user input validation functions
    #blank fields
def is_empty(value):
    if value:
        return True
    else:
        return False

#check password for spaces and length
def valid_user_entry(text):
    if " " in text:
        return False
    if len(text) < 3 or len(text) > 20:
        return False
    return True


# Define Error Codes

# Display Errors

# Complete signup form

# Comlete the task

#return errors or clear everything
@app.route('/user_signup', methods=['POST'])
def user_signup():

    #intake user's inputs from form
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    #declare error messages
    empty_field_error = "Field cannot be blank"
    username_input_error = "Username must be 3-20 alpa characters only"
    password_input_error = "Password must be 3-20 characters only, no spaces"
    password_mismatch_error = "Passwords do not match"
    email_invalid = "Please enter a valide email address (ie. you@somewhere.com)"

    #assign Error variables
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

#fail checks
# username
    if not is_empty(username):                
        username_error = empty_field_error
        return username_error
    
    if not valid_user_entry(username):
        username_error = username_input_error
        return username_error

#password
    if not is_empty(password):
        password_error = empty_field_error
        return password_error

    if not valid_user_entry(password):
        password_error = password_input_error
        return password_error

#verify password
    if not is_empty(verify_password):
       verify_password_error = empty_field_error
       return verify_password_error

    if not valid_user_entry(verify_password):
        verify_password_error = password_input_error
        return password_error

    if password != verify_password:
        return password_mismatch_error

        #verify email syntax
    if email != '':
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match == None:
            email_error = email_invalid
            return email_error
        else:
            return email_error


    # Resolve conflicts and redirect or direct user to correct
    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        template = jinja_env.get_template('form.html')
        return template.render(
        username = username,
        username_error = username_error,
        password_error = password_error,
        verify_password_error = verify_password_error,
        email_error = email_error
        )

app.run()