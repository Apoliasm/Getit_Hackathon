
class Sharing:
  def __init__(self,User,food,share_user):
    self.User = User
    self.shared_food=food
    self.share_user = share_user

  def deal(self):# 내 음식을 나눴다고 가정
    #self.User.ref=self.User.ref-self.shared_food#나눈 음식을 내 냉장고에서 제거
    self.share_user.ref.append_food(self.shared_food)
    #self.share_user.ref = self.share_user.ref+self.shared_food #나눔받은 사람 냉장고에 나눈 음식 추가
    self.User.ref.delete_food(self.shared_food)
    return self.User.ref,self.share_user.ref

  def show_food(self):
    print(self.shared_food)
    return self.shared_food

