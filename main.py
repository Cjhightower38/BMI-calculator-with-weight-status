# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Creates a BMI calculator using the rules of how BMI is calculated hences the use of both the int() and the float() my original BMI code.
# a= float(height)
# b= int(weight)
# c= int(b)/float(a*a)
# print(int(c))

# Better writen code with the health statistics.
bmi = weight / (height*height)
new_bmi = (round(bmi))

if new_bmi <= 18.5:
    print('Your BMI is ' + new_bmi + ', you are underweight.')
elif new_bmi <=24:
    print("Your BMI is " + str(new_bmi) + ", you have a normal weight.")
elif new_bmi <= 29:
    print('Your BMI is ' + str(new_bmi) + ', you are slightly overweight.' )
elif new_bmi >= 35:
    print('Your BMI is ' + new_bmi + ', you are obese.')
else:
    print('Your BMI is ' + new_bmi + ', you are clinically obese.')



