# Create a program that finds out how many times the letter ‘e’ is said in the text and then displays it as a percentage of all the letters.

test_string = "hello"

def count_vowels(string):
    num_vowels = 0
    string = string.lower()
    for char in string:
        if char in "aeiou":
           num_vowels += 1
    return num_vowels

print(count_vowels(test_string))