from flask import Flask,render_template,request,url_for,redirect
import os
import food
import User
import ref
import Sharing
application = Flask(__name__)
application.secret_key = os.urandom(24)


@application.route("/")
def First_view():
    return render_template("login.html")


@application.route("/home",methods=['POST','GET']) #login.html에서 입력값 받음 ->global 변수에 저장 -> home화면으로 넘어감
def login():
    if request.method == 'POST':
        user_name= request.form["user_name"]
        user_location = request.form["user_location"]
        r1 = ref.ref([])
        global current_user #현재 접속한 유저 정보 저장
        current_user=User.User(user_name,user_location,r1)
        return render_template("home.html",current_user = current_user)
    return render_template('home.html',current_user=current_user)


@application.route("/ref")
def ref_open():
    return render_template("ref.html")


@application.route("/reftohome",methods=['POST','GET'])
def ref_input():
    if request.method == 'POST':
        food_name = request.form['food_name']
        food_type = request.form['food_type']
        food_exp = request.form['food_exp']
        food_opened_str = request.form['food_opened']
        splited_exp = food_exp.split(sep='-')
        food1 = food.food(food_name,food_type,food_opened_str,int(splited_exp[0]),int(splited_exp[1]),int(splited_exp[2]),"www.google.com")
        current_user.ref.append_food(food1)
        return render_template("home.html",current_user=current_user)
    return redirect(url_for("login"))
if __name__ == '__main__':
    application.run("0.0.0.0",5000,debug=True)