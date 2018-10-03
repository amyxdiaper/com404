print("Where do you want to look?")

place = input() 
if (place == "in the bedroom"):
  print("Where do you want to look in the bedroom?")
  bedroom_place = input()

  if (bedroom_place == "under the bed"):
   print("Found some socks, but no battery")
  else:
   print("Found some mess, but no battery")
