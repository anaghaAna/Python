def add(value1,value2):
    return value1+value2
def multiply(c,d):
    return c*d
operation=input("enter the operation")
c=int(input("enter the first value"))
d=int(input("enter the second value"))
if operation=="add":
    print(add(c,d))
elif operation=="multiply":
    print(multiply(c,d))
else:
   print("operation invalid")
    
   