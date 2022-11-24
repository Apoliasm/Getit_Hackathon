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
        return render_template('home.html',current_user=current_user,sharelist=sharelist,my_ref=my_ref)
    return render_template('home.html',current_user=current_user,sharelist=sharelist,my_ref=my_ref)


@application.route("/ref")
def ref_open():
    return render_template("ref.html")

@application.route("/view2")
def view2():
    value=current_user.ref.view_food()
    return render_template("view2.html",value = value)

@application.route("/view3")
def view3():
    value=current_user.ref.ref_food[0].food_name
    return render_template("view3.html",value = value)

@application.route("/trade",methods = ['GET','POST'])
def success_trade():
    if request.method == 'POST':
        to_trade = request.form['food_name']
        
        for classindex,shareindex in zip(sharing_class_list,sharelist): #검색한 음식이 shared에 있으면 sharing.deal 실행
            if to_trade == shareindex['NAME']:
                
                sharelist.remove(shareindex)
                classindex.share_user = current_user  #classindex = sharing object
                classindex.deal()
                sharing_class_list.remove(classindex)
                save_to_ref = classindex.shared_food
                my_ref.append([save_to_ref.food_name, save_to_ref.food_type, save_to_ref.final_date, save_to_ref.opened]) #출력할 냉장고에 저장
                break
            
        return render_template('home.html',current_user=current_user,sharelist=sharelist,my_ref=my_ref)
    
    return render_template('home.html',current_user=current_user,sharelist=sharelist,my_ref=my_ref)
@application.route("/view3_1")
def view3_1():
    value=current_user.ref.ref_food[0].food_name
    return render_template("view3-1.html",value = value)

@application.route("/reftohome",methods=['POST','GET'])
def ref_input():
    if request.method == 'POST':
        
        food_name = request.form['food_name']
        food_type = request.form['food_type']
        food_exp = request.form['food_exp']
        food_opened_str = request.form['food_opened']
        
        food_info = [food_name,food_type,food_exp,food_opened_str]
        my_ref.append(food_info)
        
        splited_exp = food_exp.split(sep='-')
        food1 = food.food(food_name,food_type,food_opened_str,int(splited_exp[0]),int(splited_exp[1]),int(splited_exp[2]),"www.google.com")
        current_user.ref.append_food(food1)
        return render_template('home.html',current_user=current_user,sharelist=sharelist,my_ref=my_ref)
    return redirect(url_for("login"))

if __name__ == '__main__':
    ##### 초기 데이터 #####
    r1 = ref.ref([])
    r2 = ref.ref([])
    r3 = ref.ref([])
    user1 = User.User("111","A",r1)
    user2 = User.User("222","A",r2)
    user3 = User.User("333","A",r3)
    f1=food.food("사과","과일","off",2022,12,23,"www.apple.com")
    f2=food.food("상추","채소","off",2022,11,28,"www.naver.com")
    f3=food.food("우유","유제품","on",2022,11,26,"www.google.com")
    user1.ref.append_food(f1)
    user1.ref.append_food(f2)
    user2.ref.append_food(f3)
    share1 = Sharing.Sharing(user1,user1.ref.ref_food[0],None)
    share2 = Sharing.Sharing(user2,user2.ref.ref_food[0],None)
    global sharelist
    sharelist = []
    global sharing_class_list 
    sharing_class_list = []
    sharing_class_list.append(share1)
    sharing_class_list.append(share2)
    sharelist.append({"ID":share1.User.ID, "NAME":share1.shared_food.food_name,"EXP":share1.shared_food.final_date,"OPENED":share1.shared_food.opened})
    sharelist.append({"ID":share2.User.ID,"NAME":share2.shared_food.food_name,"EXP":share2.shared_food.final_date,"OPENED":share2.shared_food.opened})
    
    global my_ref
    my_ref = []
    ###초기 데이터 ###
    
    application.run("0.0.0.0",5000,debug=True)