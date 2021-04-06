def is_palindrome(word):
  #convert the word to lowercae
  word = word.lower()
  # create a string called s
  s = ""
  # This code will loop through each letter in the word 
  # variable "word". As it loops, it will takes the next # letter and append it to the "s" string.
  for letter in word:
    s += letter
    #print(s)
  if (s[::-1]) == (s[::1]):
    print("a palindrome")
  else:
    print("not a palindrome")
  # it will print the string


  

is_palindrome("annannas")
