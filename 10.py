print("hello")
mytuple =  ( "apple" ,  "banana" ,  "cherry" ) 
for x in mytuple:
 print(x)

mystr =  "banana" 
myit =  iter ( mystr ) 

print ( next ( myit ) ) 
print ( next ( myit ) ) 
print ( next ( myit ) ) 
print ( next ( myit ) ) 
print ( next ( myit ) ) 
print ( next ( myit ) )

print()
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration



myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
 class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=15:
         x=self.a
         self.a +=2
         return x
        else: 
         raise StopIteration
myclass=mynumbers()
Myiter=iter(myclass)
                
