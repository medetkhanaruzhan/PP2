f = open(r"/Users/aruzhanmedetkhan/Desktop/PP2/Lab6/dir-and-files/text.txt", "w")
numbers = [1, 2, 3, 4, 6, 4, 7, 3]
for i in range(len(numbers)):
    if i == 0:
        f.write("[")
    if i != len(numbers) - 1:
        f.write(f"{numbers[i]}, ")
    if i == len(numbers) - 1:
        f.write(f"{numbers[i]}]")
f.close()