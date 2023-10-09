from flask import Flask, render_template

app = Flask(__name__)

jobs= [
    {
        'id':1,
        'title': 'Data analyst',
        'location': 'dhaka,bd',
        'salary': 'bdt 20lacs'
    },
    {
        'id':2,
        'title': 'frontend developer',
        'location': 'dhaka,bd',
        'salary': 'bdt 10lacs'
    },
    {
        'id':3,
        'title': 'backend developer',
        'location': 'dhaka,bd',
        'salary': 'bdt 15lacs'
    },
]

@app.route('/')
def hello():
    return render_template('home.html',jobs= jobs,com_name= 'JIGAOBD')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
