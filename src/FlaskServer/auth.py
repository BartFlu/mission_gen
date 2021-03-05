from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from dacite import from_dict
from src.DataModel.usermodel import User
from flask_login import login_user, current_user, logout_user
from src.FlaskServer.db import get_db


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    db = get_db()
    username = request.form.get('username')
    password = request.form.get('password')

    user = from_dict(data_class=User, data=db.user_driver.get_user_by_username(username))
    pass_result = check_password_hash(db.user_driver.get_pass_hash(username), password)

    if user and pass_result:
        login_user(user, remember=True)
        print(current_user)
        return redirect(url_for('html_output.home'))
    else:
        flash('Please check you login details and try again.')

    return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
    return render_template('register.html')


@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    pass_check = request.form.get('password_check')
    db = get_db()

    if db.user_driver.is_username_free(username) and db.user_driver.does_email_exists(email):
        if password == pass_check:
            pass_hash = generate_password_hash(password)
            user_data = {"username": username, "email": email, "pass_hash": pass_hash}
            db.insert_user(user_data)
        else:
            flash("Passwords don't match")
            return redirect(url_for('auth.signup'))
    else:
        flash('There is already a username with that name or the email already in use.')
        return redirect(url_for('auth.signup'))
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('html_output.home'))
