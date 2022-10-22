from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where()

# mongo db Atlas
client = MongoClient('mongodb+srv://test:sparta@cluster0.6b0cooc.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.sparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# to do list 기록하기
@app.route("/todo", methods=["POST"])
def todo_post():
    todo_receive = request.form['todo_give']

    # todo_list에 모든 데이터를 받은다음에
    todo_list = list(db.todo.find({}, {'_id':False}))
    # 받은 길이의 순서대로 +1을 해서 num을 매겨준다.
    count = len(todo_list) + 1

    doc = {
        'num' : count,
        'todo' : todo_receive,
        'done' : 0
    }

    db.todo.insert_one(doc)

    return jsonify({'msg': 'to do list 등록 완료!'})

# 완료 to do list 체크하기
@app.route("/todo/done", methods=["POST"])
def todo_done():
    num_receive = request.form['num_give']
    db.todo.update_one({'num': int(num_receive)}, {'$set': {'done':1}})
    return jsonify({'msg': 'to do 완료!'})



# to do list 띄워주기
@app.route("/todo", methods=["GET"])
def todo_get():
    todo_list = list(db.todo.find({}, {'_id':False}))
    return jsonify({'todos':todo_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)