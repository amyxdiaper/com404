class Bot:

  #initial state of bot
  def __init__(self, name):
    self.name = name
    self.age = 0
    self.energy = 100
    self.shield = 100


#behaivours of bot
  def display_name(self):
    print(self.name)

  def display_age(self):
    print(self.age)

  def display_energy(self):
    print(self.energy)

  def display_shield(self):
    print(self.shield)

  def __str__(self):
    return "{} is {} years old, has {} energy and {} shield percentage".format(self.name, self.age, self.energy, self.shield) 
