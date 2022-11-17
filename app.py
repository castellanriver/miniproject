from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('p0.html')


# API

# 방명록 작성
@app.route('/p0_guestBook', methods=['POST'])
def write_guestbook():
    name_receive = request.form['name_give']
    content_receive = request.form['content_give']

    doc = {
        'name': name_receive,
        'content': content_receive,
        'likes': 0
    }

    db.p0.insert_one(doc)

    return jsonify({'msg': '저장완료!'})

# 방명록 불러오기

@app.route('/p0_guestBook', methods=['GET'])
def read_guestbook():
    comment = list(db.p0.find({}, {'_id': False}))
    return jsonify({'all_contents': comment})

# 방명록 삭제

@app.route('/p0_delete', methods=['POST'])
def delete_comment():
    name_receive = request.form['name_give']
    db.p0.delete_one({'name': name_receive})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
