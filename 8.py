class MyClass:
  x = 7

print(MyClass)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Bill", 63)
p2= Person("Gary", 17)
p3= p2.name, p2.age
print(p1.name)
print(p1.age)
print(p3)
#in this case self is p1

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Bill", 63)
p1.myfunc()

class fruit:
    def __init__(A, name, taste):
        A.name=name
        A.taste=taste
    def myfunc(A): 
        print( A.name, "is", A.taste)
F1=fruit("watermelon", "sweet")
F1.myfunc()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Bill", "Gates")
x.printname()

print()
class name:
    def __init__(by,fname,lname):
        by.fname=fname
        by.lname=lname
    def printname(by):
     print(by.fname,by.lname)
x = name("Gary", "Guo")
x.printname()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Elon", "Musk", 2019)
x.welcome()


    
