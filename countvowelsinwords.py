# create a program that can read in different words and then find which word has the most vowels. Write the output of this code to see how many times a certain letter appears in all the words

sentence = "hello, how are you?"

PUNCTUATION = "!?,.()"

# Count how many vowels using the same function from "countvowels.py"
def count_vowels(string):
    num_vowels = 0
    string = string.lower()
    for char in string:
        if char in "aeiou":
           num_vowels += 1
    return num_vowels / len(string)

# Remove any standard punctuation
# However our string is quite primitive and could do with more advanced punctuation
# PUNCTUATION is in capital letters as it is a constant (good practice)

PUNCTUATION = "!?,.()"

def remove_punctuation(input_string):
    output_string = ""
    for char in input_string:
        if char in PUNCTUATION:
            pass
        else:
            output_string += char
    return output_string

# Sentence has it's punctation removed is split into words
sentence = remove_punctuation(sentence).split(" ")

# A dictionary called most_vowels stores the decimal as it's key and the word as it's value
# E.G. { 0.5: "OX" }
most_vowels = {}

# Loop through the sentence
for word in sentence:

    # If the current key in most_vowels is < the current word we are looping through
    # Then the most_vowels key is replaced
    for key in most_vowels:
        if key < count_vowels(word):
            most_vowels = {count_vowels(word): word}
    else:

        # if most_vowels is empty then the first word is put as the biggest word
        # Gotta start somewhere
        most_vowels = {count_vowels(word): word}

# By mapping the dict_list to a list it can be accessed like a normal list
print(f"The most vowled word is '{list(most_vowels.values())[0]}'")
