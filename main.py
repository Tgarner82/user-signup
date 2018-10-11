from flask import Flask, request, redirect, render_template
import cgi
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/")
def display():
    return render_template('signup_form.html', user_name='', user_password='',
    user_verify='', user_email='', user_error='', password_error='', 
    verify_error='', email_error='')

@app.route("/", methods=['POST'])
def welcome():

    user_name = request.form['user_name']
    user_password = request.form['user_password']
    user_verify = request.form['user_verify']
    user_email = request.form['user_email']

    user_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    
    if user_name == '':
        user_error = 'Please do not leave an empty field.'
    else:
        user_name = user_name 
        if len(user_name) < 3 or len(user_name) > 20:
            user_error = 'User name must be longer than 3 and shorter than 20 characters.'
        else:
            user_name=user_name
            if user_name:
                for x in user_name:
                    if x.isspace():
                        user_error = 'Please do not use a space.'
           #if re.search(r'\s',user_name):
                    else:
                        user_name=user_name

    if user_password == '':
        password_error = 'Please do not leave an empty field.'
    else:
        user_password=user_password
        if len(user_password) < 3 or len(user_password) > 20:
            password_error = 'User name must be longer than 3 and shorter than 20 characters.'
        else:
            user_password=user_password
            if user_password:
                for x in user_password:
                    if x.isspace():
                        password_error = 'Please do not use a space'
            # if re.search(r'\s', user_password):
                    else:
                        user_password=user_password

    if user_verify == '':
        verify_error = 'Please do not leave an empty field.'
    else:
        user_verify=user_verify
        if user_verify != user_password:
            verify_error = 'Password must match.'
        else:
            user_verify=user_verify

    if user_email == '':
        user_email=user_email
    else:
        if '@' not in user_email:
            email_error = 'Missing an "@"'
        elif '.' not in user_email:
            email_error = 'Missing an "."'
        else:
            user_email=user_email
            if len(user_email) < 3 or len(user_email) > 20:
                email_error = 'Email must be longer than 3 and shorter than 20 characters.'
            else:
                user_email=user_email

    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', name=user_name)
    else:
        return render_template('signup_form.html', user_error=user_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error)

    
             
app.run()