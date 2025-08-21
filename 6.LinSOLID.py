# The Liskov Substitution Principle (LSP) states that objects of a subclass should be replaceable with 
# objects of their superclass without affecting the correctness of the program.
# In simple terms: If class B inherits from class A, we should be 
# able to use B wherever A is expected, without breaking the system.

class Bird:
    def make_sound(self):
        print("Some Generic bird Sound")

    def fly(self):
        print("This bird is flying")

class Sparrow(Bird):
    def make_sound(self):
        print("Chirp Chirp")

# Violates LSP
class Penguin(Bird):
    def make_sound(self):
        print("Honk Honk")
    
    def fly(self):
        print("Error: Penguins Cannot fly")

def make_bird_fly(bird: Bird):
    bird.fly()

sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)
make_bird_fly(penguin)


         