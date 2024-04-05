weight=int(input("enter the weight in kgs:"));
height=float(input("enter the height in meters:"));
BMI=weight/height**2
if BMI<18.5:
    print('underweight')
elif BMI<25:
    print("normal")
else:
    print("overweight")
