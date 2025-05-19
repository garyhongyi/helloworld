print("nihao")
thisset = {"apple", "banana", "cherry"}
print(thisset)

print("hello")

x="a"
print(x)

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result


def my_add(a,b):
    c= a+b;
    d=2*c;
    return d
    

print("\n\nRecursion Example Results")

#output = my_add(3,4)
#print("\n\n the add result is :")
#print(output)


tri_recursion(6)

#A lambda function that adds 10 to the number passed as a parameter and prints the result:
x=lambda a : a +  10 
print ( x ( 5 ) )

#Use this function definition to create a function that always doubles the number it is sent:


def  myfunc ( n ) : 
  return  lambda a : a * n 

mydoubler = myfunc ( 2 ) 

print ( mydoubler ( 11 ) )

#Add one more element to the cars array:
cars =  [ "Porsche" ,  "Volvo" ,  "BMW" ]
cars . append ( "Audi" )
print(cars)
