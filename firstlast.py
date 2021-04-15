# Create a function that will take in a string as a 
# parameter and return a tuple with the first letter and 
# the last letter.

test_string = "hello you"

def first_and_last(string: str):
  return string[0], string[-1]

print(first_and_last(test_string))
