from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.mystar


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
# GET
@app.route('/api/list', methods=['GET'])
def show_stars():
    movie_star = list(db.mystar.find({}, {'_id':False}).sort('like',-1))
    # sort : pymongo에서 데이터를 정렬해서 데이터를 뽑아줌.
    return jsonify({'movie_stars': movie_star})


@app.route('/api/like', methods=['POST'])
def like_star():
    name_receive = request.form['name_give']
    # 이름을 받아오고

    target_star = db.mystar.find_one({'name': name_receive})
    current_like = target_star['like']
    # 받아온 이름에서 맞는 target_star 하나를 찾아주고 그 target_star의 like를 current_like로 받는다.

    new_like = current_like + 1
    # 찾은 target_star의 current_like를 하나 올려서 new_like로 받고

    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})
    # db에 POST하는데 name이 위에서 받아온 name_receive인 것의 like를 new_like로 바꾼다.

    return jsonify({'msg': '좋아요!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    name_receive = request.form['name_give']

    db.mystar.delete_one({'name':name_receive})

    return jsonify({'msg': '영화인을 삭제했습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)