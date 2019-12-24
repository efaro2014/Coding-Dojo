# Start by creating an Animal class, and then at least 3 specific animal classes that inherit from Animal.
# (Maybe lions and tigers and bears, oh my!) Each animal should at least have a name, an age, a health level, and happiness level.
# The Animal class should have a display_info method that shows the animal's name, health, and happiness.
# It should also have a feed method that increases health and happiness by 10.

class Animal:
    def __init__(self, name, age, health_level=0, happiness_level=0):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def display_info(self):
        print(self.name)

    def feed(self, amount):
        self.happiness_level += 10
        self.health_level += 10
# In at least one of the Animal child classes you've created, add at least one unique attribute.
#  Give each animal different default levels of health and happiness.
# The animals should also respond to the feed method with varying levels of changes to health and happiness.
class Lions(Animal):
    def __init__(self, name, age,classification, health_level=0, happiness_level=0):
        super().__init__( name, age, health_level=50, happiness_level=60)
        self.classification = classification
    def feed(self, amount):
        self.health_level -= amount
        self.happiness_level += amount
class Tigers(Animal):
    def __init__(self, name, age,classification, health_level=0, happiness_level=0):
        super().__init__( name, age, health_level=50, happiness_level=60)
        self.classification = classification

    def feed(self, amount):
        self.health_level -= amount
        self.happiness_level += amount
class Beers(Animal):
    def __init__(self, name, age, classification, health_level=0, happiness_level=0):
        super().__init__(name, age, health_level=50, happiness_level=60)
        self.classification = classification

# lion1 = Lions('nan', 20, 'predator')
# lion1.display_info()

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_lion(self, name, age, classification):
        self.animals.append(Lions(name, age, classification))
        return self
    def add_tiger(self, name, age, classification):
        self.animals.append(Tigers(name, age, classification))
        return self
    def print_all_infos(self):
        print('-' * 20, self.name, '-'* 20)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 20 , 'prey').add_lion("Nala", 20 , 'prey').add_lion('Rajsh', 12, 'predator').add_lion('Rajsh', 12, 'predator').add_lion('Rajsh', 12, 'predator')
zoo1.print_all_infos()