import re

#Return a list containing every occurrence of "ai":

str = "China is a great country"
x = re.findall("i", str)
print(x)

import re

str = "China is a great country"

#Check if "USA" is in the string:

x = re.findall("USA", str)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
  
import re

str = "China is a great country"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())

import re

str = "China is a great country"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())

#在每个空白字符处进行拆分：

import re

str = "China is a great country"
x = re.split("\s", str)
print(x)
