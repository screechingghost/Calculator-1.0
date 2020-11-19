print("Hello")
print("welcome to calculator-1.0")
start=input("PRESS 'R' TO ACTIVATE OR PRESS ANY KEY TO CLOSE- CALCULATO")
try:
 if start=="R" or start=="r" :
  import math
  print("mode of calculation:")
  print("+~Add")
  print("-~Subtract")
  print("x~Multiply")
  print("/~Divide")
  print("s~Square root")
  
  l='y'
  while l=="y" or l=="Y":
   option=input("please enter your mode of calculation (+|-|x|/|s): ")
   if option=="s":
     num=float(input("enter number="))
    
   elif option=="+" or option=="-" or option=="x" or option=="X" or option=="/" :
    num1=float(input("enter first number="))
    num2=float(input("enter second number="))
   else:
     print('Invalid input please choose from above options')
   
 
    
   if option=="+":
    print(num1,"+",num2,"=",num1+num2)
   elif option=="-":
    print(num1,"-",num2,"=", num1-num2)
   elif option=="x":
    print(num1,"x",num2,"=",num1*num2)
   elif option=="/":
    print(num1,"/",num2,"=",num1/num2)
   elif option=="s" or option=="S":
    print(num,"square root is",math.sqrt(num)) 
  
   l=input("Do you have more calculation- y,n:") 
  if l=="n" or l=="N":
    
    print("Thanks For Using calculator")
  else:
   print("thanks for using calculator ")
except:
    print("Invalid Entry")  
