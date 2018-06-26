class Animal:
    import os
    def __init__(self,name,f):
        self.name = name

        self.f = f
    def get_name(self):
        self.name=self.f.read()
        return self.name
    def __def__(self):
        self.f.write(self.name)
        self.f.close()
        print("对象呗销毁")

dog=Animal("",open("name.txt","r"))
print(dog.get_name())
dog.f= open("name.txt","w")
dog.f.write("旺财")
print("+++++++")
xiaoming=Animal("","ds")
