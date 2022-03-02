
f=open("file.txt","r")
s=f.read()
f.close()

f=open("copy.txt","w")
f.write(s)
f.close()
