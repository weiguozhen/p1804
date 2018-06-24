try:
    print("name")
    try:
        for i in rane(1,10):
            print(i)
    except (TypeError,NameError):
        print("有问题")
except IOError as a :
    print(a)
