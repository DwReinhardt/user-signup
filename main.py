#import items
from flask import Flask, request, redirect
import cgi
import os
import jinja2
import re
#*****************************

# Using Templates
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
def valid_user_pword(text):
    if " " in text:
        return False
    if len(text) < 3 or len(text) > 20:
        return False
    return True
'''
#check for valid email address
def email_valid(email):
    addressToVerify ='email'
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
    if match == None:
        return False
'''
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
    password_input_error = "password must be 3-20 characters only, no spaces"
    password_mismatch_error = "Passwords do not match"

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

#password
    if not is_empty(password):
        password_error = empty_field_error
        return password_error

    if not valid_user_pword(password):
        password_error = password_input_error
        return password_error

#verify password
    if not is_empty(verify_password):
       verify_password_error = empty_field_error
       return verify_password_error

    if not valid_user_pword(verify_password):
        verify_password_error = password_input_error
        return password_error

    if password != verify_password_error:
        return password_mismatch_error

#return errors or clear everything
    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        username_error = ''
        password_error = ''
        verify_password_error = ''
        email_error = ''
        return redirect('/welcome?username={0}'.format(username))
    else:
        return template.render('form.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)



'''
# create route to validate the field entries
@app.route('/validate_entries', methods=['POST'])
def validate_entries():


@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)

@app.route('/validate_entries')
'''

app.run()