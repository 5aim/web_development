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

# 댓글 저장하기
@app.route("/fanboard", methods=["POST"])
def homework_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.fanboard.insert_one(doc)
    return jsonify({'msg':'응원완료!'})

# 전체 댓글 보여주기
@app.route("/fanboard", methods=["GET"])
def homework_get():
    comment_list = list(db.fanboard.find({},{'_id':False}))
    return jsonify({'comments':comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)