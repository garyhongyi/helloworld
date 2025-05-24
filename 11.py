def myfunc():
  x = 100
  print(x)
myfunc()

def  myfunc ( ) : 
  global x#if you stuck in a local 
  x =  100

myfunc ( )

print ( x )

def  greeting ( name ) : 
  print ( "Hello, "  + name )



def  greeting ( name ) : 
  print ( "Hello, "  + name )
 
person1 =  { 
  "name" :  "Bill" , 
  "age" :  63 , 
  "country" :  "USA" 
}

import datetime

x = datetime . datetime . now ( ) 
print ( x )

import json

# Python object (dictionary): 
x =  { 
  "name" :  "Bill" , 
  "age" :  63 , 
  "city" :  "Seatle" 
}

# Convert to JSON: 
y = json.dumps ( x )

# The result is a JSON string: 
print ( y )
