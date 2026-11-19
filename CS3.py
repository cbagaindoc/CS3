#Level 1: Base parent class
class Animal:
 def __init__(self, kingdom = "Animalia"):
  self.kingdom = kingdom
 def eat(self):
  print("Consuming food for energy.")
#Level 2: Child of Animal and Parent of Dog
class Mammal(Animal):
 def __init__(self, kingdom, warm_blooded: True):
  super().__init__(kingdom) #passes kingdom up to Animal constructor
  self.warm_blooded = warm_blooded
 def nurse_young(self):
  print("Feeding milk to offspring.")
#Level 3: Sub class of Mammal
class Dog(Mammal):
 def __init__(self, kingdom, warm_blooded, breed, name):
  super().__init__(kingdom, warm_blooded) #Ask Mammal to handle kingdom and warm_blooded initialization
  self.breed = breed
  self.name = name
 def bark(self):
  print(f"{self.name} the {self.breed} says Woof!")
#Testing the Multi-level Biology Chain
my_dog = Dog("Animalia", True, "Shih Tzu", "Bruno")
#Accessing the attributes inherited from 3 levels
print("Kingdom: ", my_dog.kingdom)
#print(f"Kingdom: {my_dog.kingdom})
print("Warm-blooded: ", my_dog.warm_blooded)
print("Breed: ", my_dog.breed)
#Executing methods inherited from all 3 levels
my_dog.eat()
my_dog.nurse_young()
my_dog.bark()
