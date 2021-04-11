# Write a program that takes the input of three numbers and prints their sum, product, and quotient.
# Takes input text


number=input("Enter a number: ")
number2=input("Enter a second number: ")
number3=input("Enter a third number: ")

def countnumbers(number, number2, number3):
   return int(number)+int(number2)+int(number3)

def multiplynumbers(number, number2, number3):
   return int(number)*int(number2)*int(number3)

def quotientnumbers(number, number2, number3):
   return int(number)/int(number2)/int(number3)

print(countnumbers(number, number2, number3))
print(multiplynumbers(number, number2, number3))
print(quotientnumbers(number, number2, number3))