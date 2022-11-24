class User:
  def __init__(self,ID,Location,ref):
    self.ID = ID
    self.my_location = Location
    self.ref=ref
  
  def __str__(self):
    return "ID : {}, location : {}, 냉장고 음식 : {}".format(self.ID, self.my_location, self.ref)