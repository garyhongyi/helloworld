#tryBlocks allow you to test blocks of code to find bugs.

#exceptBlocks allow you to handle errors.

#finallyThe try and except blocks allow you to execute code regardless of the outcome of the try and except blocks.

try:
  print(x)
except:
  print("An exception occurred")

try : 
  print ( x ) 
except NameError : 
  print ( "Variable x is not defined" ) 
except : 
  print ( "Something else went wrong" )

#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



price = 52
txt = "The price is {} dollars"
print(txt.format(price))


quantity = 3
itemno = 567
price = 52
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 52
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Porsche", model = "911"))
