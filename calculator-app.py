while True:
    a = float(input("enter the first value:"))
    b = float(input("enter the second value:"))
    c = str(input("enter the operator(+,-,*,/):"))
    if (c=="+"):
        print(a+b)
    elif (c=="-"):
        print(a-b)
    elif (c=="*"):
        print(a*b)
    elif (c=="/"):
         if(b==0):
            print("the value of b is zero")
    else:
        print(a/b)
    choice = input("yes or no")
    if (choice=="yes"):
        continue
    else:
        print("chal bhag")
    break                    

