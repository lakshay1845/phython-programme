print("BMI calculator")
weight=int(input("Enter your weight"))
height=int(input("Enter your height"))
if weight <=0 :
   print("weight must be positive")
if height <=0:
   print("height must be positive")

BMI = weight/(height*height)
if BMI<18.5:
   print("Category: underweight")
elif BMI< 25:   
   print("Category: Normal wight")
elif BMI< 30:
   print("Category: Overweight") 
else: 
   print("Category: obesity")

