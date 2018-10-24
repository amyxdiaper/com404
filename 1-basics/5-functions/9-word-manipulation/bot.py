def in_a_box(word):
  print("*" * (len(word) + 10))
  print("*", word, "*")
  print("*" * (len(word) + 10))


def lower_case(word):
  print(word.lower())


def upper_case(word):
  print(word.upper())


def mirrored(word):
  print(word, "|" ,word[::-1])


def repeat(word):
  print("Please enter number of repitions")
  user_num = int(input())
  for count in range (0, user_num, 1):
   if (count % 2 == 0):
     print(word.lower())
   else:
     print(word.upper())


def run():
  print("Please enter a word")
  word = str(input())
  print("""Please choose an option
  1- put word in an ascii box
  2- show word in lower case letters
  3- show word in upper case letters
  4- show word mirrored
  5- repeat the word as many times as you like, alternating between upper and lower case""")
  user_option = int(input())
  if (user_option == 1):
    print(in_a_box(word))
  elif (user_option == 2):
    print(lower_case(word))
  elif (user_option == 3):
    print(upper_case(word))
  elif (user_option == 4):
    print(mirrored(word))
  elif (user_option == 5):
    print(repeat(word))
  else:
    print ("I am not sure what you entered!")

run()
