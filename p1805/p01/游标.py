f=open("1.txt","w+")
f.write("举头望明月\n")
f.write("低头思故乡\n")
f.close()
f= open("1.txt","rb+")
c=f.readline()
p=f.tell()
print("读的第一行内容是%s"%c)
print("游标位置是%d"%p)
f.seek(0,0)
print(f.readline())
f.seek(-3,2)
print(f.tell)
f.close()



