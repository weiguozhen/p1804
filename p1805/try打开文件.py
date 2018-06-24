i=input("倾诉如要打开的文件")
f=open(i,"r")
try:
    print(a)
    s=f.read()
    print(s)
except Exception as b:
    print(b)
finally:
    f.close()
print(f.closed)
print("___-")
