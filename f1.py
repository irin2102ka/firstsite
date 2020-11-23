# -*- coding: utf-8 -*-
import os
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    user = "Ирина"
    return render_template('index.html', title='Домашняя страница', 
                           username=user)

@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('new_news.html', news=news_list)    
    
   
@app.route('/first_page')
def first():
    name= url_for('static', filename='img/picture.jpg')
    return render_template('picture.html', name=name)

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('forms.html' )
    
    
    
    
    elif request.method == 'POST':
        print(request.form.get('email'))
        print(request.form.get('password'))
        print(request.form.get('file'))
        print(request.form.get('about'))
        print(request.form.get('accept'))
        print(request.form.get('sex'))
        return "Форма отправлена"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)