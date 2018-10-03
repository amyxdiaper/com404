print("Where do you want to look?")

place = input() 
if (place == "in the bedroom"):
  print("Where do you want to look in the bedroom?")
  bedroom_place = input()

  if (bedroom_place == "under the bed"):
   print("Found some socks, but no battery")
  else:
   print("Found some mess, but no battery")

elif (place == "in the bathroom"):
  print("Where do you want to look in the bathroom?")
  bathroom_place = input()

  if (bathroom_place == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found some mess but no battery")

elif (place == "in the lab"):
  print("Where do you want to look in the lab?")
  lab_place = input()

  if (lab_place == "on the table"):
    print("Found the battery!")
  else:
    print("Found some tools but no battery")

else:
  print("I dont know where that is but we'll keep looking!")
