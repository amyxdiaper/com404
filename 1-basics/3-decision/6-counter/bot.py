print("Please enter first number")
first_number = int(input())
print("Please enter second number")
second_number = int(input())
print("Please enter third number")
third_number = int(input())

evens = 0
odds = 0

if (first_number % 2 == 0):
  evens = evens + 1
else:
  odds = odds + 1

if (second_number % 2 == 0):
  evens = evens + 1
else:
  odds = odds + 1

if (third_number % 2 == 0):
  evens = evens + 1
else:
 odds = odds + 1

print("There are", evens," even numbers and", odds,"odd numbers.")
