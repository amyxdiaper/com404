MAX_FACES = 10

# ask user for number of robot
print("How many ascii robots should I draw?")

# read users response for number of robots
robots = int(input())

robots_displayed = 0

# display users number of robots
if(robots < MAX_FACES):
  print("Here I go:")
  for robots_displayed in range(robots):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
    robots_displayed = robots_displayed + 1
# display max 10 robots
else:
  for robots_displayed in range(MAX_FACES):
    print("#########")
    print("#       #")
    print("# O   O #")
    print("|   V   |")
    print("|  ---  |")
    print("|_______|")
    robots_displayed = robots_displayed + 1

print("Done!")
