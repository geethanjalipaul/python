import filecmp

c=filecmp.cmp("file.txt","copy.txt")
print(c)
