# create a program that takes input text and outputs any words with three or more consonants.

inputText = input()
inputText = inputText.lower()


for char in inputText:
  if char not in "aoie":
    print(char)