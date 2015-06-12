from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

from wevesi.forms.access import LoginForm, SignupForm
from wevesi.models.user import UserObj

base_listener = Blueprint('base_listener', __name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(userid):
    """This loads a user"""
    return UserObj.get(userid)


@base_listener.route('/')
def index():
    return render_template('index.html')


@base_listener.route('/login', methods=['GET', 'POST'])
def login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        email = form_login.email.data
        passwd = form_login.password.data
        user = UserObj.login(email, passwd)
        if user:
            login_user(user)
            flash('Logged in successfully', 'success')
            return redirect(url_for('index'))
        else:
            flash('Unable to verify username and password', 'danger')
    return render_template('login.html', form=form_login)


@base_listener.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    logout_user()
    flash('Disconected successfully', 'success')
    return redirect(url_for('index'))


@base_listener.route('/signup', methods=['GET', 'POST'])
def signup():
    form_signup = SignupForm()
    if form_signup.validate_on_submit():
        name = form_signup.name.data
        email = form_signup.email.data
        passwd = form_signup.password.data
        passwd_repeat = form_signup.password_repeat.data
        if passwd == passwd_repeat:
            user = UserObj.create(name, email, passwd)
            if user:
                flash('User created', 'success')
                return redirect(url_for('index'))
        else:
            flash('Passwords doesn\'t match', 'danger')
    return render_template('signup.html', form=form_signup)

