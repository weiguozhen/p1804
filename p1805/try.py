class Test(object):
    def __init__(self):
        self.switch="open"
    def div(self,a,b):
        try:
            return a/b

        except Exception as a:
            if self.switch=="open":
                print("出现异常%s"%a)
            #else:
             #   raise
        else:
            print("没意向后")
        finally:
            print("hahahha")
t=Test()
#t.switch="close"
print(t.div(2,1))

