from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.wdsffte.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/seob')
def seob():
   return render_template('seob.html')

@app.route('/kong')
def kong():
   return render_template('kong.html')

@app.route('/yun')
def yun():
   return render_template('yun.html')

@app.route('/hyun')
def hyun():
   return render_template('hyun.html')

@app.route('/eon')
def eon():
   return render_template('eon.html')

@app.route('/ha')
def ha():
   return render_template('ha.html')

# 김인섭 -----------------------------------------------------------------------------

@app.route("/seob/guestbook", methods=["POST"])
def seob_post():
    id_receive = request.form['id_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'id':id_receive,
        'name':name_receive,
        'comment':comment_receive
    }

    db.seob.insert_one(doc)

    return jsonify({'msg':'작성 완료!'})

@app.route("/seob/guestbook", methods=["GET"])
def seob_get():
    comment_list = list(db.seob.find({}, {'_id': False}))
    return jsonify({'comments':comment_list})

@app.route('/seob/guestbook/', methods=['DELETE'])
def seob_delete():
    id_receive = request.form['id_delete']
    db.seob.delete_one({'id':id_receive})
    return jsonify({'msg':'삭제했습니다.'})

# 김재현 ----------------------------------------------------------------------------------------
# 유저 읽기

@app.route('/user/1', methods=["POST"])
def comment_save():
       comment_receive = request.form['comment_give']
       comment_data = {
          "comment":comment_receive
       }
       db.hyun.insert_one(comment_data)
       return jsonify({ 'msg' : "작성완료 "})


@app.route('/user/1/comments', methods=["GET"])
def comment_get():
       comment_list = list(db.hyun.find({}, {"_id" : False}))
       return jsonify({'comments' : comment_list})

# 이태언 ----------------------------------------------------------------------------------------
@app.route("/eon/guestbook", methods=["POST"])
def introduce_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.eon.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'name':name_receive,
        'comment':comment_receive,
        'num':count
    }

    db.eon.insert_one(doc)
    return jsonify({'msg':'Thanks for your comment!'})

@app.route("/eon/guestbook", methods=["GET"])
def introduce_get():
    comment_list = list(db.eon.find({}, {'_id': False}))
    return jsonify({'comments':comment_list})

@app.route("/eon/guestbook2", methods=["POST"])
def introduce_num():
    num_receive = request.form["num_give"]
    db.eon.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})
# 김채하 ----------------------------------------------------------------------------------------
@app.route("/ha/guestbook", methods=["POST"])
def ha_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.ha.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num':count,
        'name':name_receive,
        'comment':comment_receive,
        'done':0
    }
    db.ha.insert_one(doc)
    return jsonify({'msg':'저장 완료!'})

@app.route("/ha/guestbook/done", methods=["POST"])
def delete_comment():
    num_receive = request.form['num_give']
    db.ha.update_one({'num':int(num_receive)},{'$set':{'done':1}})
    return jsonify({'msg': '삭제완료'})

@app.route("/ha/guestbook", methods=["GET"])
def ha_get():
    comment_list = list(db.ha.find({}, {'_id':False}))
    return jsonify({'comments':comment_list})
# 변시윤 ----------------------------------------------------------------------------------------
## 등록
@app.route("/yun/guestbook", methods=["POST"])
def introduction_post():
    name_receive = request.form["name_give"]
    guestComment_receive = request.form["guestComment_give"]
    date_receive = request.form["date_give"]
    dateId_receive = request.form["dateId_give"]
    ## 추가기능 - num 받아오기
    guestbookList = list(db.bsy.find({}, {'_id': False}))
    count = len(guestbookList) + 1
    doc = {
        'name': name_receive,
        'comment': guestComment_receive,
        'date': date_receive,
        'num': count,
        'read': 0,
        'selfId': dateId_receive + str(count)
    }
    db.yun.insert_one(doc)

    return jsonify({'msg':'😘'})


## 불러오기
@app.route("/yun/guestbook", methods=["GET"])
def introduction_get():
    guestComment_list = list(db.yun.find({},{'_id':False}))
    # print(db.bsy.find())
    return jsonify({'guestComments':guestComment_list})


## 삭제하기
@app.route("/yun/guestbook/remove", methods=["POST"])
def introduction_remove():
    selfId_receive = request.form["selfId_give"]
    db.yun.delete_one({'selfId': selfId_receive})
    return jsonify({'msg': '삭제완료'})


## 추가기능 - 읽음 확인
@app.route("/yun/guestbook/read", methods=["POST"])
def introduction_read():
    selfId_receive = request.form["selfId_give"]
    db.yun.update_one({'selfId': selfId_receive}, {'$set': {'read': 1}})
    return jsonify({'msg': '방명록 확인 ✅'})
# ----------------------------------------------------------------------------------------
if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)