import os
s = open("./Index.md", "r").readlines()

for i in s:
    temp = "".join(i.split(" ")[1:])
    os.mkdir(temp)

