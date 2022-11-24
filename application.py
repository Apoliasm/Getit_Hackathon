from flask import Flask,render_template
import os
import datetime
import webbrowser
import User
import ref
import Sharing
import food

application = Flask(__name__)
application.secret_key = os.urandom(24)
test_User =User.User("test","대구",ref.ref(food.food("당근","야채",2022,11,27,""))) 


@application.route("/")
def First_view():
    return render_template("test.html")

@application.route("/view2")
def view2():
    value=test_User.ref.ref_food.food_name
    return render_template("view2.html",value = value)

@application.route("/view3")
def view3():
    value=test_User.ref.ref_food.food_name
    return render_template("view3.html",value = value)

@application.route("/view3_1")
def view3_1():
    value=test_User.ref.ref_food.food_name
    return render_template("view3-1.html",value = value)

if __name__ == '__main__':
    application.run("0.0.0.0",5000)

