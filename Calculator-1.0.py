print("Hello")
print("welcome to calculator")
start=input("PRESS 'R' TO ACTIVATE OR PRESS ANY KEY TO CLOSE- CALCULATO")
if start=="R":
  import math
  print("mode of calculation:")
  print("+~ADD")
  print("-~Subtract")
  print("x~multiply")
  print("/~divide")
  print("s~square root")



  option=input("please enter your mode of calculation (+|-|x|/|s): ")

  num1=float(input("enter first number="))
  if option!="S":
   num2=float(input("enter second number="))
   if option=="+":
    print(num1,"+",num2,"=",num1+num2)
   elif option=="-":
    print(num1,"-",num2,"=", num1-num2)
   elif option=="x":
    print(num1,"x",num2,"=",num1*num2)
   elif option=="/":
    print(num1,"/",num2,"=",num1/num2)
  else:
    print(num1,"square root is",math.sqrt(num1))

else:
   print("PLS Type R ")
