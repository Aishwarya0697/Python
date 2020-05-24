
def div_zero(func):   #division
    def wrapper (x,y):
        if y==0:
            print("cant be divide by zero")
            return
        return func(x,y)
    return wrapper

#this function add two number
def add(x,y):
    return x+y

#this function sub two number
def sub(x,y):
    return x-y

#this function mul two number
def mul(x,y):
    return x*y

#this function div two number
@div_zero
def div(x,y):
    return x/y

while True:
    print("selection process")
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("0.stop")
    try:
        choice=int(input("enter your choice"))
      

        #this function add two number
        
        if choice==0:
            break
            
        num1=int(input("enter first number"))
        num2=int(input("enter second number"))
        
        if choice==1:
            print("num1+num2=",add(num1,num2))

        elif choice==2:
            print("num1-num2=",sub(num1,num2))

        elif choice==3:
            print("num1*num2=",mul(num1,num2))

        elif choice==4:
            print("num1/num2=",div(num1,num2))
            
        else:
            print("your input is not valid please enter num between 1 to 4")
            continue

    except Exception as e:
        print("dont enter your input in str format")
        print(e) 

