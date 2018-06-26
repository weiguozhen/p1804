from inspect import isgeneratorfunction #检测是否是生成器
def hanshu(a,b):
    while a<b:
        yield a    #用于创建生成器generator
        a=a+1
v=hanshu(1,5)
print(isgeneratorfunction(hanshu))

#print(type(v))
#print(v)
next(v)#逐一查看生成器中的内容
#next(v)
for i in v: #遍历生成器中的内容
    print(i)





#print(v)
