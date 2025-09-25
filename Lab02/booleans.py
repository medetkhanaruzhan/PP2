#example1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#example2
a=200
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#example3
print(bool("Hello"))
print(bool(15))

#example4
x="hello"
y=15
print(bool(x))
print(bool(y))

#example5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#example6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

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
