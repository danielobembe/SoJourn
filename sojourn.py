from flask import Flask, render_template 

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)