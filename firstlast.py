# Create a function that will take in a string as a 
# parameter and return a tuple with the first letter and 
# the last letter.

word = "hello you"

def findFirstandLast(word):
  word = word.lower()
  s = ""
  for letter in word:
     s += letter
  print(s[0])
  print(s[-1])

findFirstandLast(word)