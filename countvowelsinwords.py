# create a program that can read in different words and then find which word has the most vowels. Write the output of this code to see how many times a certain letter appears in all the words

words = "hello, how are you?"

words = words.split(" ")

for word in words:
    num_vowels=0
    for char in word:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    print (num_vowels)
