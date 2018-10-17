#define first function
def sum_ages_of_friends(Applejack, Rainbowdash, Buttershine):
 #calculate the ages of the friends
 total = Applejack + Rainbowdash + Buttershine
 return total


def calc_avg_ages_of_friends(Applejack, Rainbowdash, Buttershine):
 #calculate the average of the ages
 average = sum_ages_of_friends(Applejack, Rainbowdash, Buttershine) / 3
 return average


def run():
 print("Enter an age for Applejack")
 Applejack = int(input())
 print("Enter an age for Rainbowdash")
 Rainbowdash = int(input())
 print ("Enter an age for Buttershine")
 Buttershine = int(input())
 print("Please choose sum or average of ages")
 choice = str(input())

 if(choice == "sum"):
   print("The total of their ages is", sum_ages_of_friends(Applejack, Rainbowdash, Buttershine))
 elif(choice == "average"):
   print("The average of their ages is", calc_avg_ages_of_friends(Applejack, Rainbowdash, Buttershine))
 

run()
