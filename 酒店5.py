def huanying():
    print("酒店管理系统".center(30,"^"))
    print("1.信息录入\n2.查询全部入住客人\n3.查询指定客户入住信息\n4.修改客户信息\n5.删除用户信息\n6.普通结账\n7.办理会员卡\n8.会员卡结账")
    print("*"*36)
huanying()



import time

l=[]
def luru():
    print("客人信息录入".center(30,"*"))
    print("标注单间100/天、豪华单间150/天、标准双人间150/天、豪华双人间200/天、总统套房400/天")
    a=input("请输入客人姓名:")
    b=input("请输入客人身份证号码:")
    c=int(input("请输入入住天数:"))
    d=int(input("请输入入住标准/价格:"))
    e=time.asctime()
    print("_"*30)
    dic={'name':a,'card':b,'day':c,'price':d,'time':e}
    l.append(dic)
    print("您输入的名字是%s\n您输入的身份证号是：%s\n您输入的入住天数是：%d\n您输入的价格是：%d\n您录入的时间是：%s"%(dic['name'],dic['card'],dic['day'],dic['price'],dic['time']))


def all1():
    print("显示全部客人信息".center(30,'*'))
    for i in l:
        print("客人的姓名：%s"%i["name"])
        print("客人的身份证号：%s"%i['card'])
        print("客人的入住天数：%d"%i['day'])
        print("客人的入住标准/价格是：%d"%i['price'])
        print("客人的入住时间是%s"%i['time'])
        print("*"*30)
        if len(l) == 0:
            print("没有入住客人")


def zhiding():
    print("显示指定客人信息".center(30,"*"))
    a=input("请输入要查找客户的姓名")
    for i in l:
        if i['name'] == a:
            print("客户的姓名是：%s"% i ['name'])
            print("客户的身份证号是：%s"%i['card'])
            print("客户的入住天数是：%d"%i['day'])
            print('客户的入住标准/价格是：%d'%i['price'])
            print("客户的入住时间是%s"%i['time'])
            print("*"*30)



def xiugai():
    print("修改客户信息".center(30,'*'))
    q=input("请输入要修改的客户姓名")
    for i in l:
        if i['name'] == q:
            i['name']=input("请输入要修改的名字：")
            i['card']=input("请输入要修改的身份证号：")
            i['day']=int(input("请输入要修改的入住天数："))
            i['price']=int(input("请输入要修改的价格："))
            i['time']=input("请输入要修改的时间")
            print("修改成功".center(30,"*"))



def del1():
    print("删除客户信息".center(30,'^'))
    c=input("请输入要修改客户的姓名")
    for i in l:
        if i['name']==c:
            l.remove(i)
            print("删除成功")



def jiezhang():
    user=input("请输入入住人姓名")
    for i in l:
        if i ['name'] == user:
            s=i['price']*i['day']
            return s



c=[]
def huiyuan():
    a=input("创建账号")
    b=input("创建密码")
    zidian={"zhanghao":a,'mima':b}
    c.append(zidian)
    print("会员卡创建成功")


def hykjz():
    o=input("请输入账号")
    p=input("请输入密码")
    for i in c:
        if i['zhanghao']==o and i['mima']==p:
            print("登陆成功")
            a=input("请输入入住人姓名")
            for u in l:
                if u['name']==a:
                    s=u['price']*u['day']*0.8
                    print("您应付的价格是%d"%s)
                    break
        else:
            print("输入错误请重新输入")


def tuichu ():
    print("欢迎下次光临")


while True:
    m=input("请输入选择的服务")
    if m=="1":
        luru()
    elif m=="2":
        all1()
    elif m=="3":
        zhiding()
    elif m=="4":
        xiugai()
    elif m=="5":
        del1()
    elif m=="6":
        s=jiezhang()
        print("您应付价格是%d"%s)
    elif m=='7':
        huiyuan()
    elif m=="8":
        hykjz()
    elif m=="9":
        tuichu()
        break













