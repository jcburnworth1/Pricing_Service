## Import libraries
from flask import Blueprint, request, session, url_for, render_template, redirect
from models.users.user import User, UserErrors

## Create item Blueprint
user_blueprint = Blueprint('users', __name__)

## Register User Endpoint
@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(email, password)
            session['email'] = email
            return email
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/register.html')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return email
        except UserErrors.UserError as e:
            return e.message

    return render_template('users/login.html')