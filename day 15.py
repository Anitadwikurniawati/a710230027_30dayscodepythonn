from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def eat(self):
        pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def eat(self):
        print("Sparrow eating")

    def fly(self):
        print("Sparrow flying")

class Penguin(Bird):
    def eat(self):
        print("Penguin eating")

def make_bird_fly(bird):
    if isinstance(bird, FlyingBird):
        bird.fly()
    else:
        print(f"{type(bird).__name__} can't fly")

sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  
make_bird_fly(penguin)  
