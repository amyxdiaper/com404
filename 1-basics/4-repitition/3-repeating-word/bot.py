# ask user for their word
print("Please enter your word:")

# read users word
word = input()

# determine length of users word
length = len(word)

word_displayed = 0

print("Processing word... learning...")

# display users word the same number of times as it has letters
if(length < 100):
  for word_displayed in range(length):
    print(word)
    word_displayed = word_displayed + 1

print("Word successfully learnt!")
