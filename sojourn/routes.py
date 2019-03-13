from flask import render_template, url_for, flash, redirect
from sojourn.forms import RegistrationForm, LoginForm
from sojourn.models import User, Post
from sojourn import app

posts = [
    {
        'author':'Dani Obem',
        'title':'Blog post 1',
        'content':'Content of first post',
        'date_posted':'April 29, 2018'
    },
    {
        'author':'Ricki Oslo',
        'title':'Blog post 2',
        'content':'Content of second post',
        'date_posted':'April 20, 2018'
    }
]

@app.route('/')
def index():
    return render_template('index.html', title='Home', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)