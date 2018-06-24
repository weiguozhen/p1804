class MyError(Exception):
    def __init__(self,name,age):
        self.name=name
        self.age=age
def get_pwd():
    pwd = input("输入密码")
    if len(pwd)<6:
        raise MyError("密码小雨6",12)
try:
    get_pwd()
except Exception as re:
    print("遇到异常%s"%re)

