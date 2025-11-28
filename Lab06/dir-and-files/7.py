f = open(r"/Users/aruzhanmedetkhan/Desktop/PP2/Lab06/dir-and-files/text.txt", "r")
new = open(r"/Users/aruzhanmedetkhan/Desktop/PP2/Lab06/dir-and-files/to_copy.txt", "w")

for line in f:
    new.write(line)

f.close()
new.close()