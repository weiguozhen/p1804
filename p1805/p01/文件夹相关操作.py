import os
#os.mkdir("house")#当前路径 创建文件夹
#os.mkdir("../girl")#相对或绝对路径，+文件夹
#pwd
p=os.getcwd()#得到当前路径
print("当前路径是%s"%p)
#修改默认的路径
p=os.chdir("./house")
print("修改之后的默认路径是%s"%p)
f = open("1.txt","w")
os.mkdir('xiaohua')#创建到了新路径下
os.rmdir("xiaohua")
os.chdir("../")
#当文件夹空的时候，可以用os.rmdir删除
#当文件夹不空的时候用以下方法删除
import shutil
shutil.rmtree("house")

