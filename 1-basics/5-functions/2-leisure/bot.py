# create a new function get the user to choose an activity
def activity():
  print("Please enter an activity")
  leisure = str(input())

  if leisure == ("watch movie"):
    print("Watching a movie sounds like fun!")
  elif leisure == ("play"):
     print("I have lots of toys to play with!")
  else:
    print("I am not sure if i will like it but i will give it a try!")

activity() 
