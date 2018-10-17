#ask the user a character, a total number of characters and a whole number
print("Please enter a character to display")
character = str(input())

print("Please enter total number of characters")
total = int(input())

print("Please enter a whole number")
whole_number = int(input())

#create a function to run the program
def run():

 for count in range (1,total+1,1):
#total is plus one because we are not including 0
    
    
    if (count % whole_number == 0):
      print(character, end="")
    else:
      print("-", end ="")
#if the whole number is a multiple of the total, display a character, if not, display a dash
run()
