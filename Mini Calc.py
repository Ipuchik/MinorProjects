import math

def add(a,b):
    x = a+b
    return x

def sub(a,b):
    x = a-b
    return x

def mult(a,b):
    x = a*b
    return x

def div(a,b):
    x = a/b
    return x

def roots(a,b):
    x = a**(1/b)
    return x

def power(a,b):
    x = a**b
    return x

def degSin(a):
 return math.sin(a*math.pi/180)

def degCos(a):
 return math.cos(a*math.pi/180)

def degTan(a):
 return math.tan(a*math.pi/180)

while True:
    
    print("Operators are \n add \n sub \n div \n mult \n roots \n Power \n degSin \n degCos \n degTan \n stop")

    operator=str(input("Enter Operator :"))
    x = int(input("Enter first value :"))
    y = int(input("Enter second value :"))

    if (operator == "add"):
        answer = add (x,y)
    elif (operator == "sub"):
        answer = sub (x,y)
    elif (operator == "mult"):
        answer = mult (x,y)
    elif (operator == "div"):
        answer = div (x,y)
    elif (operator == "roots"):
        answer = roots(x,y)
    elif (operator == "power"):
        answer = power (x,y)
    elif (operator == "degSin"):
        answer = degSin (x)
    elif (operator == "degCos"):
        answer = degCos (x)
    elif (operator == "degTan"):
        answer = degTan (x)
    elif (operator == "stop"):
        break
    print(answer)

    

      



