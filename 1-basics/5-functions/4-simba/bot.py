def roar(num_roars):

 for count in range(0,num_roars,1):
   print("roar!")
   
 if(num_roars < 3):
   print("cough cough!")
 elif(num_roars >= 3):
   print("ROAR!!!")

  # The following are calls to the function for testing purposes
roar(1)
roar(3)
