# For loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through a string
for letter in "banana":
    print(letter)

# For loop with break
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# For loop with continue
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# Using range in a for loop
for x in range(6):
    print(x)

# While loop
i = 1
while i < 6:
    print(i)
    i += 1

# While loop with break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# While loop with continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Function with no arguments
def say_hello():
    print("Hello from a function")

say_hello()

# Function with one argument
def greet(name):
    print("Hello, " + name)

greet("Alice")

# Function that returns a value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum:", result)

# Simple class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

p1 = Person("John", 36)
p1.introduce()

# Modify object property
p1.age = 40
p1.introduce()

# Delete object property
del p1.age
# print(p1.age)  # Would cause an AttributeError

# Inheritance example
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self):
        print(f"I am {self.name}, {self.age} years old, studying at {self.school}.")

s1 = Student("Anna", 22, "ABC University")
s1.introduce()
