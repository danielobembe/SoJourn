from flask import Flask, render_template 

app = Flask(__name__)

posts = [
    {
        'author':'',
        'title':'',
        'content':'',
        'date_posted':''
    },
    {
        'author':'',
        'title':'',
        'content':'',
        'date_posted':''
    },
    {
        'author':'',
        'title':'',
        'content':'',
        'date_posted':''
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