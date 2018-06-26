import random




class PetShop:
    def __init__(self,animal_factory=None):
        self.pet_factory = animal_factory
    def show_pet(self):
        pet = self.pet_factory.get_pet()
        print("This is a lovely",pet)
        print("It says",pet.speak())
        print("It eats",self.pet_factory.get_food())
class Dog:
    def speak(self):
        return "woof"
    def __str__(self):
        return "dog"

class Cat:
    def speak(self):
        return "meow"
    def __str__(self):
        return "Cat"
class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "dog food"


def get_factoruy():
    return random.choice([DogFactory,CatFactory])()

if __name__=="__main__":
    shop=PetShop()

    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("="*20)
