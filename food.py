import datetime
import webbrowser
import ref
import Sharing
import User

class food:
    def __init__ (self,name,type,opened,year,month,day,link):
        self.food_name = name
        self.food_type = type
        self.opened = opened #음식 개방 여부(bool type)
        self.final_date = datetime.datetime(year ,month ,day)
        
        self.coupang = link
    def __str__(self) -> str:
        return 'food_name = {}, food_type = {}, final_date = {}, coupanglink = {}'.format(self.food_name,self.food_type,self.final_date,self.coupang)
    
    def view_date(self) ->datetime.datetime: #남은 유통기한 보여줌
        return self.final_date
    
    def link_coupang(self): # 쿠팡 파트너스 => 쿠팡 링크에 연결# RETURN값은 쿠팡 링크의 음식
        open = webbrowser.open_new(self.coupang)
        print(open)
    
    def check_expiration (self): #유통기한 임박 체크 #ref클래스의 list를 하나씩 돌면서 체크 후 출력 
        now = datetime.datetime.now()
        diff = now - self.final_date
        diff_day = diff.days
        if(diff_day <=3): #유통기한이 얼마 남지 않았으면 남은 날짜 출력 
            return diff_day 
    

        
if __name__ == '__main__':
    f1 = food("food1","type1",2022,11,21,"http://www.google.com")
    
    print(f1)
    print(f1.final_date)
    now = datetime.datetime.now()
    diff = now - f1.final_date
    print(diff.days)
    r1 = ref.ref([])
    r2 = ref.ref([])
    u1 = User.User("id1","loc1",r1)
    u1.ref.append_food(f1)
    u2 = User.User("id2","loc1",r2)
    s1 = Sharing.Sharing(u1,f1,u2)
    s1.show_food()
    s1.deal()
    print(u1.ref.ref_food)
    print(u1.ref.ref_food)
    print(u2.ref.ref_food[0])
    