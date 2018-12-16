from flask import Flask
from flask import request
from flask import render_template
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/')

def my_form():
    return render_template("my_form.html")





@app.route('/', methods=['POST'])
def my_form_post():
    html = request.form['html']
    soup = BeautifulSoup(html, 'html.parser')
    return(soup)



if __name__ == '__main__':
    app.run()