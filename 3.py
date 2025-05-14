#from dictionary
#Create three dictionaries, and then create a dictionary that contains the other three dictionaries:
child1 =  { 
  "name"  :  "Phoebe Adele" , 
  "year"  :  2002 } 
child2 =  { 
  "name"  :  "Jennifer Katharine" , 
  "year"  :  1996 } 
child3 =  { 
  "name"  :  "Rory John" , 
  "year"  :  1999 }

myfamily =  { 
  "child1"  : child1 , 
  "child2"  : child2 , 
  "child3"  : child3 }
print(myfamily)

#dict()New dictionaries can also be created using the constructor:
thisdict =  dict ( brand = "Porsche" , model = "911" , year = 1963 ) 
# Note that the keywords are not string literals. 
# Note that the equal sign is used instead of a colon to assign the value. 
print ( thisdict )

#elifKeywords are Python's way of saying "if the previous condition wasn't true, then try this condition."
a =  66 
b =  66 
if b > a : 
  print ( "b is greater than a" ) 
elif a == b : 
  print ( "a and b are equal" )

a=67^3
b=35^4
if b>a:
    print("b is greater than a")
elif a==b:
    print("a is equal to b")
elif a>b:
    print("a is greater than b")
#The else keyword captures anything that is not captured by the previous condition.
a =  200 
b =  66 
if b > a : 
  print ( "b is greater than a" ) 
elif a == b : 
  print ( "a and b are equal" ) 
else : 
  print ( "a is greater than b" )
#Single-line if else statement:
a =  200 
b =  66 
print ( "A" )  if a > b else  print ( "B" )
#Test whether a is greater than b, or whether a is greater than c:
a =  200 
b =  66 
c =  500 
if a > b or a > c : 
  print ( "At least one of the conditions is True" )
#As long as i is less than 7, print i:
i =  1 
while i <  7 : 
  print ( i ) 
  i +=  1
#Sets i = 1
#Enters the while loop because i < 7 is True
#Prints the current value of i
#Increments i by 1 using i += 1
#Repeats until i is no longer less than 7
  
#break:We can stop the loop even if the while condition is true if we use the while statement:
#Exit the loop when i equals 3:
i =  1 
while i <  7 : 
  print ( i ) 
  if i ==  3 : 
    break 
  i +=  1

