import json

# some JSON:
x =  '{ "name":"Bill", "age":63, "city":"Seatle"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


import json

print(json.dumps({"name": "Bill", "age": 63}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
x


import json

x = {
  "name": "Bill",
  "age": 63,
  "married": True,
  "divorced": False,
  "children": ("Jennifer","Rory","Phoebe"),
  "pets": None,
  "cars": [
    {"model": "Porsche", "mpg": 38.2},
    {"model": "BMW M5", "mpg": 26.9}
  ]
}

print(json.dumps(x))
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

#Use separatorsthe parameter to change the default delimiter:

json . dumps ( x , indent = 4 , separators = ( ". " ,  " = " ) )

#RegEx can be used to check whether a string contains a specified search pattern.



import re 

txt =  "China is a great hih country" 
x = re.search ( "^China.*country$" , txt )
if (x):
  print("YES! We have a match!")
else:
  print("No match")

