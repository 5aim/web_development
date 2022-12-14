from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.linkmemo


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['GET'])
def listing():
    articles = list(db.linkmemo.find({}, {'_id':False}))
    return jsonify({'all_articles':articles})


## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # data에 url receive를 받기 때문에 아래와 같이 따로 써 줄 필요가 없다.
    # url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=81888' 탑건 메버릭 url

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    og_title = soup.select_one('meta[property="og:title"]')['content']
    og_image = soup.select_one('meta[property="og:image"]')['content']
    og_description = soup.select_one('meta[property="og:description"]')['content']

    doc = {
        'title':og_title,
        'image':og_image,
        'desc':og_description,
        'url':url_receive,
        'comment':comment_receive
    }

    db.linkmemo.insert_one(doc)

    return jsonify({'msg':'포스팅을 완료하였습니다'})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5001,debug=True)