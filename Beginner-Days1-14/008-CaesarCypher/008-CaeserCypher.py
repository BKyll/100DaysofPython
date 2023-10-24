import art
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

again = True

print(art.logo)

def caesar(text, shift, direction):
  if direction == 'decode':
    shift = -shift
  originalText = [*text]
  message = ""
  
  for char in originalText:
    if char in alphabet: 
      message += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
    elif char in numbers:
      message += numbers[(numbers.index(char) + shift) % len(numbers)]
    else:
      message += char
      
  print(f'The {direction}d text is "{message}".')

while again == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(text, shift, direction)

  againInput = input("\nContinue? Yes or No\n").lower()
  if againInput == "no":
    print("Goodbye")
    again = False