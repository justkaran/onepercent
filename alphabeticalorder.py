word = "hello you"

def alphabeticalorder(word):
  word = word.lower()
  s = ""
  for letter in word:
     s += letter
  print(s[0])
  print(s[-1])

findFirstandLast(word)