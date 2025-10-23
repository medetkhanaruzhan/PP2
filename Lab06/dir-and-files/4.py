f = open(r'/Users/aruzhanmedetkhan/Desktop/PP2/Lab06/dir-and-files/text.txt', 'r')
count = 0
for i in f:
    count += 1
print(count)
f.close()