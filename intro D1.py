#this is the first time officially start to study python,
#for the future week, i will sort out all the skills needed and put them into different docs.

#how to print
print("Hello, World!")

#syntax of python
if  5  >  2 : 
  print ( "Five is greater than two!" )#you need indentation (space) to make it right
  print ("five is greater than two")# you need to use the same amount of indentation in a code block

#variables in python
x =  5 
y =  "Hello, World!"
#you can use both '' or ""
#calculation
x=5
y=6
print(x+y)
#Create a variable outside a function and use it inside the function:
x =  "awesome"

def myfunc ( ) : 
  print("Python is "+  x )

myfunc()
#test the type of the data:
x="aaaa"
print(type(x))

x =  10    # int 
y =  6.3   # float 
z =  2j    # complex
print ( type ( x ) ) 
print ( type ( y ) ) 
print ( type ( z ) )
print(x)

x =  10  # int 
y =  6.3  # float 
z =  1j  # complex 

# Convert an integer to a floating point number
 
a =  float ( x ) 

# Convert a floating point number to an integer
 
b =  int ( y ) 

# Convert an integer to a complex number:
 
c =  complex ( x ) 

print ( a ) 
print ( b ) 
print ( c ) 

print ( type ( a ) ) 
print ( type ( b ) ) 
print ( type ( c ) )



#Get the characters from position 2 to position 5 (not included):
b =  "Hello, World!" 
print ( b [ 2 : 5 ] )

#Get the characters from position 5 to position 1, counting from the end of the string:
b =  "Hello, World!" 
print ( b [ - 5 : - 2 ] )

#The len() function returns the length of a string:
a =  "Hello, World!" 
print ( len ( a ) )

#The strip() method removes leading and trailing whitespace characters:
a =  "Hello, World! " 
print ( a . strip ( ) )  # returns "Hello, World!"

#lower() returns a lowercase string:
a =  "Hello, World!" 
print ( a . lower ( ) )

#replace() replaces a string with another string:
a =  "Hello, World!" 
print ( a . replace ( "World" ,  "Kitty" ) )

#Checks the following text for the presence of the phrase "ina":
txt =  "China is a great country" 
x =  "ina"  in txt
print ( x )

#Use format()the method to insert a number into a string:
age =  63  
txt =  "My name is Bill, and I am {}" 
print ( txt . format ( age ) )

quantity =  3 
itemno =  567 
price =  49.95 
myorder =  "I want {} pieces of item {} for {} dollars." 
print ( myorder . format ( quantity , itemno , price ) )

#You can use index numbers {0}to ensure that parameters are placed in the correct placeholders:

quantity =  3 
itemno =  567 
price =  49.95 
myorder =  "I want to pay {2} dollars for {0} pieces of item {1}." 
print ( myorder . format ( quantity , itemno , price ) )

#Return the third, fourth, and fifth items:
thislist =  [ "apple" ,  "banana" ,  "cherry" ,  "orange" ,  "kiwi" ,  "melon" ,  "mango" ] 
print ( thislist [ 2 : 5 ] )

#Change the second item:
thislist =  [ "apple" ,  "banana" ,  "cherry" ] 
thislist [ 1 ]  =  "mango" 
print ( thislist )

#Check if "apple" exists in the list:
thislist =  [ "apple" ,  "banana" ,  "cherry" ] 
if  "apple"  in thislist : 
  print ( "Yes, 'apple' is in the fruits list" )

#Insert the item as the second position:
thislist =  [ "apple" ,  "banana" ,  "cherry" ] 
thislist . insert ( 1 ,  "orange" ) 
print ( thislist )

#thislist =  [ "apple" ,  "banana" ,  "cherry" ] 
thislist . remove ( "banana" ) 
print ( thislist )

#pop()Method deletes the specified index (if no index is specified, it deletes the last item):
thislist =  [ "apple" ,  "banana" ,  "cherry" ] 
thislist . pop ( ) 
print ( thislist )#you can also use 'del'

#Append list2 to list1:

list1 =  [ "a" ,  "b"  ,  "c" ] 
list2 =  [ 1 ,  2 ,  3 ] 

for x in list2 : 
  list1 . append ( x ) 

print ( list1 )


