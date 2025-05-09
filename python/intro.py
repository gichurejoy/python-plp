num1=int(input("input a number"))
num2=int(input("input a number"))

sign=input("-,+,*,/")

if sign=='-':
    result=num1-num2
    print(f"{num1}-{num2}={result}")

elif sign=='+':
    result=num1+num2
    print(f"{num1}+{num2}={result}")

elif sign=='*':
    result=num1*num2
    print(f"{num1}*{num2}={result}")

elif sign=='/':
    result=num1/num2
    print(f"{num1}/{num2}={result}")