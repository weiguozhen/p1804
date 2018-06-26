def funout(out=1):
    outlist = [out]
    def funin():
        outlist[0]+=1
        print(outlist[0])
    return funin
funout()()
def waibu(out=1):
    def neibu():
        nonlocal out
        out+=1
     #   return "自定义"
    return neibu
#c1=waibu()
#print(c1())
#c1()
#c1()
c2=waibu()
print(c2())
