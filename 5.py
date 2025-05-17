print("nihao")
thisset = {"apple", "banana", "cherry"}
print(thisset)

print("hello")

x="a"
print(x)

#using if
a =  66 
b =  66 
if b > a : 
  print ( "b is greater than a" ) 
elif a == b : 
  print ( "a and b are equal" )

#you can have more than one trigger
a =  200 
b =  66 
c =  500 
if a > b and c > a : 
  print ( "Both conditions are True" )

#difference between or and and
a =  200 
b =  66 
c =  500 
if a > b or a > c : 
  print ( "At least one of the conditions is True" )
x =  52

if x >  10 : 
  print ( "Above ten," ) 
  if x >  20 : 
    print ( "and also above 20!" ) 
  else : 
    print ( "but not above 20." )
#As long as i is less than 7, print i:



i=1
while i<=4:
  print(i)
  i +=1

  
i =  1 
while i <  7 : 
  print ( i ) 
  if i ==  3 : 
    break 
  i +=  1


i =  1 
while i <  6 : 
  print ( i )
  i +=  1 
else : 
  print ( "i is no longer less than 6" )
  print()

fruits =  [ "apple" ,  "banana" ,  "cherry" ] 
for x in fruits : 
  print ( x )
  print()

#By using forloops, we can execute a group of statements for each item in a list, tuple, set, etc

fruits =  [ "apple" ,  "banana" ,  "cherry" ] 
for x in fruits : 
  print ( x )  
  if x ==  "banana" : #If x is "banana", then exit the loop:
    break
    print()

for x in  range ( 10 ) : #rang(10)is 0-9
  print ( x )
#range(3, 10), which means the value is 3 to 10 (but not including 10)
  print()
#每隔三个进一个
  for x in  range ( 3 ,  50 ,  6 ) : 
   print ( x )

