class LivingBeing:
    def breathe(self):
        return "Breathing"

class Animal(LivingBeing):
    def eat(self):
        return "Eating"

class Bird(Animal):
    def fly(self):
        return "Flying"

class Human(LivingBeing):
    def think(self):
        return "Thinking"

class SuperHuman(Human, Bird):
    def show_powers(self):
        return "Flying and Thinking"

superhuman = SuperHuman()
print(superhuman.breathe())   
print(superhuman.eat())        
print(superhuman.fly())        
print(superhuman.think())      
print(superhuman.show_powers())  
