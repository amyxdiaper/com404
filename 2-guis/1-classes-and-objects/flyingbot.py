from superbot import SuperBot

class FlyingBot(SuperBot):

  def __init__(self, name):
    super().__init__(name)
    self.hover = 0

  def display_hover(self):
    print(self.hover)



 def get_hover_distance():
   return self.hover

  def set_hover_distance(distance):
    self.hover = hover
