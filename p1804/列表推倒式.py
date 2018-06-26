b = [i for i in range(1,5)]
print(b)
#列表推导式
#以列表形式呈现
a= (i for i in range(1,5))
#迭代器
print(type(a))
print(next(a))
for i in a:
    print(i)
