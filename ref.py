class ref:
  def __init__(self, ref_food):
    self.ref_food = ref_food

  def view_food(self):
    print(self.ref_food)
    return self.ref_food

  def append_food(self,Food):
    self.ref_food.append(Food)
  
  def delete_food(self,Food):
    self.ref_food.remove(Food)
  
  def share_update(self,share):
    self.ref_food=self.ref_food-share.show_food()#전체 있는 것중 나눈 음식 삭제
  
  def __str__(self):
    return self.ref_food