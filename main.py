# create a program that outputs the number of vowels in a sentence

# Takes input text
str="Please enter a string as you wish"

def countvowels(str):
    num_vowels=0
    for char in str:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

print(countvowels(str))


     