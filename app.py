from random import *

class Human:
  health = 30
  name = ""
  def __init__(self, name):
      self.name = name

  def eat(self):
      self.health+=5

myHuman = Human("Hassan")
myHuman.eat()
# print(myHuman.health)

class Ninja(Human):
    health = 10
    def __init__(self, name):
        Human.__init__(self, name)

    def meditate(self):
        self.health+=5

    def backstap(self, obj):
       obj.health-=10

kevTheNinja = Ninja("Kevin")
kevTheNinja.eat()
kevTheNinja.backstap(myHuman)
# print(myHuman.health)

class Wizard(Human):
    health = 25
    magicPower = 0
    study = randint(1, 3)
    def __init__(self, name):
        Human.__init__(self, name)

    def fireball(self, obj):
        obj.health -= self.magicPower

leroyTheDragonMaster = Wizard("Rahul")
# print(leroyTheDragonMaster.study)

class Warrior(Human):
    health = 40
    armor = 10

    def armorUp(self, obj):
        obj.armor += 5
    def sheildAlly(self, obj):
        obj.health += 5
        if obj.armor < 5:
         obj.armor -= 5
        else:
         print "error"

troyAKAbadMother_shutYourMouth = Warrior("Troy")
print(troyAKAbadMother_shutYourMouth.armor)
troyAKAbadMother_shutYourMouth.sheildAlly(Warrior)
print(troyAKAbadMother_shutYourMouth.armor)
troyAKAbadMother_shutYourMouth.armorUp(Warrior)
troyAKAbadMother_shutYourMouth.armorUp(Warrior)
print(troyAKAbadMother_shutYourMouth.armor)
