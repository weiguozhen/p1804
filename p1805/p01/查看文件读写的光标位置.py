f= open("1.txt","rb+")
f.seek(2,0)
s=f.tell()
print("文件 读取的开始位置，偏移2:%d"%s)
f.seek(2,1)
#从当前位置 读取 偏移数据
s=f.tell()
print("文件读取的当前位置偏移2：%d"%s)
f.seek(-4,2)#冲文件末尾开始
s=f.tell()
print("文件读取的从末尾开始 偏移 -2：%d"%s)
f.close()

