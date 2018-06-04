f=open ("2.txt","w")
f.write("静夜思\n")
f.write("床前明月光\n")
f.write("疑似地上霜\n")
f.write("举头望明月\n")
f.write("低头思故乡\n")
f.close()
'''
f=open("2.txt",'r')
c=f.read()
print(c)
f.close()

f=open("2.txt","r+")
f.write('哈哈')
f.close()

f=open("2.txt","r")
c=f.read()
print(c)
f.close()




f=open("2.txt","r")
c=f.read()
f.seek(0,0)
for i in c:
    f.read(1)
    p=f.tell()
    print("读的字是%s，光标位子在%s"%(i,p))
f.close()



import os
def shanchu(n):

    os.remove(n)
user=input("请输入删除的文件")

shanchu(user)

f=open("2.txt",'r+')
c=f.readlines()

print(c)
for i in c:

    print(i[:len(i)-1],"*")
f.close()

f=open("2.txt",'a+')
f.write("|")
for i in c:

    f.write(i)

f.close()
'''

f = open("2.txt",'r')
a=f.readline()
print(a)
c=f.tell()
print(c)
a=f.readline()
print(a)
c=f.tell()
print(c)
a=f.readline()
print(a)
c=f.tell()
print(c)
a=f.readline()
print(a)
c=f.tell()
print(c)
a=f.readline()
print(a)
c=f.tell()
print(c)
f.seek(0,0)
g=f.read(5)
print(g)
a=f.read()
f.seek(0,0)
j=0
for i in a :
   f.read(1)
   n=f.tell()
   print("字是%s,游标位置是%s"%(i,n))
   j=j+1
   print(j)



'''

def hanshu(n):
    f=open(n,'w+')
    f.write("哈哈哈")
    c=f.read()
    print(c)
    f.close()
name=input("请输入文件名")
hanshu(name)

import os
def shanchu(n):
    os.remove(n)
user=input("请输入要删除的文件")
shanchu(user)

import os
def gaiming(a,b):
    os.rename(a,b)
user=input('请输入要改的文件名')
us=input("请输入要修改成的名字")
print(us)
gaiming(user,us)


#import os
#os.mkdir("haha")


import shutil
def shanchu(n):
    shutil.rmtree(n)
user=input("请输入删除文件夹的名字")
shanchu(user)

import os
def xinjian(n):
    os.mkdir(n)
user=input("输入文件名")
xinjian(user)

import os
def cc(path):
    if os.getcwd==path:
        os.chdir(path)
        print(os.getcwd())
    else:
        os.mkdir(path)
        print(os.getcwd())
        os.chdir(path)
        print(os.getcwd())
user=input("输入路径")
cc(user)
'''
