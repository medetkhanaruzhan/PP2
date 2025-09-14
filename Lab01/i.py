#1
import random
print(random.randrange(1, 10))

#2
x = int(1)    # x will be 1
y = int(2.8)    # y will be 2
z = int("3")    # z will be 3

#3
x = float(1)    # x wil be 1.0
y = float(2.8)    # y will be 2.8
z = float("3")    # z will be 3.0
w = float("4.2")    # w will be 4.2 

#4
x = str("s1") # x will be 's1'
y = str(2) # y will be '2'
z = str(3.0) # z will be '3.0'

#5
print("Hello")
print('Hello')

#6
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#7
a = "Hello"
print(a)

# 8
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# 9
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# 10
a = "Hello, World!"
print(a[1])

# 11
for x in "banana":
    print(x)

# 12
a = "Hello, World!"
print(len(a))

# 13
txt = "The best things in life are free!"
print("free" in txt)

# 14
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# 15
txt = "The best things in life are free!"
print("expensive" not in txt)

# 16
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# 17
b = "Hello, World!"
print(b[2:5])

# 18
b = "Hello, World!"
print(b[:5])

# 19
b = "Hello, Wolrd!"
print(b[2:])

# 20
b = "Hello, World!"
print(b[-5:-2])

# 21
a = "Hello, World!"
print(a.upper())

# 22
a = "Hello, World!"
print(a.lower())

# 23
a = " Hello, Wolrd! "
print(a.strip()) # returns "Hello, World!"

# 24
a = "Hello, World!"
print(a.replace("H", "J"))

# 25
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', 'World!']

# 26
a = "Hello"
b = "World"
c = a + b
print(c)

# 27
a = "Hello"
b = "World"
c = a + " " + b 
print(c)

# 28
#wrong 
# age = 36
# txt = "My name is John, I am " + age 
# print(txt)

# 29
age = 36 
txt = f"My name is Jonh, I am {age}"
print(txt)

# 30
price = 59
txt = f"The price is {price} dollars"
print(txt)

#31
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#32
txt = f"The price is {20 * 59} dollars"
print(txt)

#33
# txt = "We are the so-called "Vikings" from the north."

#34
txt = "We are the so-called \"Vikings\" from the north." 