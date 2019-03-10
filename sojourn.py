from flask import (
    Flask, render_template, url_for, flash, redirect
)
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a20943a0515d374b3280ca50627ed5da'

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

if __name__ == '__main__':
    app.run(debug=True)