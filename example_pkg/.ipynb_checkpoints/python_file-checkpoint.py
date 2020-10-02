class class_name:
  def __init__(self, name):
    self.name = name

  def myfunc(self):
    print("Hello my name is " + self.name)


p1 = class_name("John")
p1.myfunc()