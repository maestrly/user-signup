from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def display_signup_form():
    return render_template('index.html', username="", username_error='', password='', password_error='', verify_password='', verify_password_error='', email='', email_error='')


@app.route('/', methods=['POST'])
def validate_form():

    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    verify_password = cgi.escape(request.form['verify_password'])
    email = cgi.escape(request.form['email'])

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    #Username is empty
    if not username:
        username_error = "Username cannot be empty"

    #Username is invalid
    elif len(username) < 3 or len(username) > 20:
        username_error = "This is a not valid username"

    #Password is empty
    if not password:
        password_error = "Password cannot be empty"

    #Password is not valid
    elif len(password) < 3 or len(password) > 20:
        password_error = "Not a valid password"

    #Passwords don't match
    if password != verify_password:
        verify_password_error = "The passwords do not match"

    #Email is invalid
    if email:
        if "@" and "." not in email:
            email_error = "Not a valid email"
        elif " " in email:
            email_error = "Not a valid email"

    #If form is valid
    if not username_error and not password_error and not verify_password_error and not email_error:
        usersuccess = username
        return redirect('/valid-form?usersuccess={0}'.format(usersuccess))
    else:
        return render_template('index.html', username=username, username_error=username_error, password=password, password_error=password_error, verify_password=verify_password, verify_password_error=verify_password_error, email=email, email_error=email_error)



@app.route('/valid-form')
def valid_form():
    usersuccess = request.args.get('usersuccess')
    return render_template('welcome.html', usersuccess=usersuccess)


app.run()
