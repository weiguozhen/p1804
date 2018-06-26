def wai(fun):
    def nei(name):
        if name == "员工":
            fun()
        else:
            print("此功能给内部员工使用")
        #return "欢迎使用"
    return nei
@wai
def f1():
    print("======f1")
@wai
def f2():
    print("=======f2")
@wai
def f3():
    print("=======f3")
@wai
def f4():
    print("========f4")
f1("员工")
'''
def wai(fun):
    def nei(name):
        if name == "员工":
            fun()
        else:
            print("无法访问")
        return "欢迎使用"
    return nei
def hanshu():
    user = input ("输入要访问的服务")
    if user == "a" :
        return a

user = input("输入身份")
print(wai(hanshu())(user))
'''




#user=input("请输入姓名")
#f1(user)
#f2(user)
#f3(user)
#f4(user)
ZZ
