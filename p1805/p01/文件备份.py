def self_cp(oname):
    old_file=open(oname,"rb+")
    p=oname.rfind(".")
    name=oname[:p]
    namek=oname[p:]
    new_file= open(name+"副本"+namek,"wb+")
    while True:
        c= old_file.read(1024)
        if len(c)==0:
            break
    old_file.close()
    new_file.close()
n= input("输入要备份的文件")
self_cp(n)

