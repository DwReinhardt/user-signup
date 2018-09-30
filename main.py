#import items
from flask import Flask, request, redirect, render_template
import re #used for email format validation string
#*****************************

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('form.html')

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

#return errors or clear everything
@app.route('/', methods=['POST'])
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
    email_invalid = "Please enter a valid email address (ie. you@somewhere.com)"

    #assign Error variables
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

#FAIL CHECKS
# username: field will either be empty or invalid...it cannot be both
    if not is_empty(username):                
        username_error = empty_field_error

    if not valid_user_entry(username):
        username_error = username_input_error

#password: field will either be empty or invalid...it cannot be both
    if not is_empty(password):
        password_error = empty_field_error

    if not valid_user_entry(password):
        password_error = password_input_error

#verify password: field will either be empty or invalid...it cannot be both
    if not is_empty(verify_password):
       verify_password_error = empty_field_error

    if not valid_user_entry(verify_password):
        verify_password_error = password_input_error

#ensure both submitted passwords are identical
    if password != verify_password:
        verify_password_error = password_mismatch_error

#verify email syntax: taken from web source after searching for a common email validation function
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    
    if email != '' and match == None:
        email_error = email_invalid

# Resolve conflicts and redirect or direct user to correct
    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return welcome(username)
    else:
        return render_template('form.html',
            username = username,
            username_error = username_error,
            password_error = password_error,
            verify_password_error = verify_password_error,
            email_error = email_error
            )

#Successful sign-up!!
def welcome(text):
    username = text
    return render_template('welcome.html', username = username)

app.run()