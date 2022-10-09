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
@app.route('/api/list', methods=['GET'])
def show_stars():
    movie_star = list(db.mystar.find({}, {'_id':False}).sort('like',-1))
    # sort : like 역순으로 불러와줌. pymongo에서 정렬에서 데이터를 뽑아줌.
    return jsonify({'movie_stars': movie_star})


@app.route('/api/like', methods=['POST'])
def like_star():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'like 연결되었습니다!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'delete 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)