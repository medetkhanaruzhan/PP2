import os

path = input("Enter path: ")

print("\nDirectories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

print("\nFiles:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)

print("\nAll items:")
for name in os.listdir(path):
    print(name)