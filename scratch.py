def validate_entries():

    #intake user's inputs from form
    username = request.form('username')
    password = request.form('password')
    verify_password = request.form('verify_password')
    email = request.form('email')

    #error messages
    empty_field_error = "Field cannot be blank"
    username_input_error = "Username must be 3-20 alpa characters only"
    password_input_error = "password must be 3-20 characters only, no spaces"
    password_mismatch_error = "Passwords do not match"

    # Error variables
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    #user input validation
        #blank fields
    def is_empty(str):
    if str == "":
        return True
    else:
        return False

    if username == '':
        username_error = empty_field_error
        return username_error
    
    if password == '':
        password_error = empty_field_error
        return password_error

    if verify_password == '':
        verify_password_error = empty_field_error
        return verify_password_error



    #invalid input: username & password
    def valid_user_pword(text):
    if " " in text:
        return False
    if len(text) < 3 or len(text) > 20:
        return False
    return True
 

    #password & verify password mismatch
    if not password == verify_password:
        verify_password_error = password_mismatch_error
        return verify_password_error

    #invalid email
    addressToVerify ='email'
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

    if match == None:
        print('Bad Syntax')
        raise ValueError('Bad Syntax')

    if not username_error and not password_error and not password_validate_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('main.html', username_error=username_error, username=username, password_error=password_error, password=password, password_validate_error=password_validate_error, password_validate=password_validate, email_error=email_error, email=email)

            username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
