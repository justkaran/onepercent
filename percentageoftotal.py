#Create a program that finds out how many times the letter ‘e’ is said in the text and then displays it as a percentage of all the letters.

string = "hello"


def countchars(string):
    num_letters= 0
    for letters in string:
      num_letters = num_letters + 1
    return num_letters

print(countchars(string), "Chars in total")

def countvowels(string):
    num_vowels=0
    for letters in string:
        if letters in "eE":
          num_vowels = num_vowels+1
    return num_vowels
print(countvowels(string), "Vowel/s")


print(countvowels(string)/countchars(string)*100, "Percent vowels compared to total chars")