#Booleans
#example1
print(10 > 9)  #True
print(10 == 9) #False
print(10 < 9)  #False

#example2
a=200
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#example3
print(bool("Hello")) #True
print(bool(15)) #True

#example4
x="hello"
y=15
print(bool(x))
print(bool(y))

#example5
bool("abc") #True
bool(123) #True
bool(["apple", "cherry", "banana"]) #True

#example6
bool(False) #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({}) #False

#example7
class myclass():
      def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#example8
def myFunction() :
    return True

print(myFunction())

#example9
def myFunction() :
    return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#example10
x = 200
print(isinstance(x, int))
