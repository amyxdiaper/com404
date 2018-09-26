# Read in user data
print("How old are you?")
age = int(input())
print("you are" ,age, "years old")

print("What is your height in m?")
height = float(input())
print("Your height is", height, "m")

print("What is your weight in kg?")
weight = float(input())
print("Your weight is", weight, "kg")

BMI = weight / (height*height)

print("your BMI is",BMI,"")
