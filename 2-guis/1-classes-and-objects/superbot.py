from bot import Bot

class SuperBot(Bot):

  def __init__(self, name):
    super().__init__(name)
    self.super_power_level = 100

  def display_super_power_level(self):
    print(self.super_power_level)
    
