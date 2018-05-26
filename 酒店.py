import time
import random
def huanying():
    print("酒店管理系统".center(30,"^"))
    print("1.信息录入\n2.查询全部入住客人\n3.查询指定客户入住信息\n4.修改客户信息\n5.删除用户信息\n6.普通结账\n7.办理会员卡/8折\n8.会员卡结账\n9.退出")
    print("*"*36)



#--------------------------------------------------欢迎
w=[]

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

#--------------------------------------------------录入
def all1():
    print("显示全部客人信息".center(30,'*'))
    for i in l:
        print("客人的姓名：%s\n客人的身份证号：%s\n客人的入住天数：%d\n客人的入住标准/价格是：%d\n客人的入住时间是：%s"%(i['name'],i['card'],i['day'],i['price'],i['time']))
        print("*"*30)
        if len(l) == 0:
            print("没有入住客人")
#-------------------------------------------------显示全部

def zhiding():
    print("显示指定客人信息".center(30,"*"))
    a=input("请输入要查找客户的姓名")
    for i in l:
        if i['name'] == a:
            print("客人的姓名：%s\n客人的身份证号：%s\n客人的入住天数：%d\n客人的入住标准/价格是：%d\n客人的入住时间是：%s"%(i['name'],i['card'],i['day'],i['price'],i['time']))
        elif len(l) == 0:
            print("没有任何入住客人")
            print("*"*30)
#--------------------------------------------------查找指定

def cccc():
    print("会员卡结账".center(30,"*"))
    a=input("请输入客户身份证号")

    for q in l:
        if q['card']==a:
            a=input('请输入账号:')
            b=input("请输入密码:")
            for p in w:

                if p['zhanghao']==a and p['mima']==b:
                    print("登陆成功")
                    c=p['vip']-q['price']*q['day']*0.8
                    d=q['price']*q['day']*0.8
                    p['vip']=p['vip']-d
                    print('您应付金额是:%d\n会员卡余额是：%d'%(d,c))




#-----------------------------------------------会员卡结账




def xiugai():
    print("修改客户信息姓名".center(30,'*'))
    q=input("请输入要修改的客户姓名:")
    for i in l:
        if i['name'] == q:
            i['name']=input("请输入要修改的名字：")
            i['card']=input("请输入要修改的身份证号：")
            i['day']=int(input("请输入要修改的入住天数："))
            i['price']=int(input("请输入要修改的价格："))
            print("修改成功".center(30,"*"))


#--------------------------------------------------修改

def del1():
    print("删除客户信息".center(30,'^'))
    c=input("请输入要修改客户的姓名")
    for i in l:
        if i['name']==c:
            l.remove(i)
            print("删除成功")
#-------------------------------------------------删除


def jie():
    user=input("请输入入住人身份证号")
    for i in l:
        if i ['card'] == user:
            s=i['price']*i['day']
            print(s)
#------------------------------------------------结账



def huiyuan():

    print("会员账号创建".center(30,'*'))
    a=input("创建账号")
    b=input("创建密码")
    x=random.randint(1,3)
    print("正在办理请稍后...\n")
    time.sleep(x)
    print("正在办理请稍后...\n")
    time.sleep(x)
    print("会员卡创建成功")
    v=int(input('请输入充值金额'))
    zidian={"zhanghao":a,'mima':b,"vip":v}

    w.append(zidian)
#---------------------------------------会员卡
def tuichu ():
    print("欢迎下次光临")



#----------------------------------------退出









