# Create a program that finds out how many times the letter ‘e’ is said in the text and then displays it as a percentage of all the letters.

string = "hello"


def countvowels(string):
    num_vowels=0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

print(countvowels(string))