def funout(out=1):
    outlist = [out]
    def funin():
        outlist[0]+=1
        print(outlist[0])
    return funin
ain=funout(5)
print(id(ain))
ain()
ain()
cin = funout()
print(id(cin))
cin()
def test(out):  #  闭包
    def test_in(num_in):
        print("里边的数字是%d"%num_in)
        return out+num_in
    return test_in
a=test(1)(2)
print(a)
