'''1. create a basic class:
Define a class called Person with attributes like name,age, and address.
Initialize the class with an instance and print the attributes.'''

class Person():
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    
    def print_attributes(self):
        print(self.firstname, self.lastname, self.age)
        
    def greet(self):
        print(f'Hi, my name is {self.firstname}.')
        
    def introduce(self):
        print(f'My name is {self.firstname} {self.lastname}, and I am {self.age} years old.')
    
        
x = Person('Pete', 'Pall', 44)
x.print_attributes()
x.greet()
x.introduce()

'''
2. Create methods in a class: In the Person class,
add methods like introduce() and greet().
The introduce() method should print a brief introduction about the person and
the greet() method should print a friendly greeting.
'''

'''
3. Polymorphism: Define a class Pet with an attribute called name and a method speak().
Create two subclasses Dog and Cat that inherit from the Pet class.
Override the speak() method in the Dog and Cat classes to return a string that is specific to each type of pet.
'''

class Pet():
    def speak(self):
        print('I am a pet')
        
class Dog(Pet):
    def speak(self):
        print('I am a pet dog')
        
class Cat(Pet):
      def speak(self):
        print('I am a pet cat')
        
x = Pet()
y = Dog()
z = Cat()
x.speak()
y.speak()
z.speak()