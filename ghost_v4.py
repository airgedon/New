str_input = input("Enter string: ")

print("Input string = ", str_input)

i = len(str_input) - 1
while i >= 0:
  print(str_input[i])
  i = i - 1
 
 
 
 
#  -----------------------------------------------------------




string = input("Please enter string: ")

numbers = 0
uppercase = 0
lowercase = 0
other_char = 0

for char in string:
  if char.isdigit():
    numbers += 1
  elif char.isupper():
    uppercase += 1
  elif char.islower():
    lowercase += 1
  else:
    other_char += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Numbers:", numbers)
print("Other characters:", other_char)




# ----------------------------------------------------------------------



while True:
  str_input = input("Please enter string: ")

  if str_input == "done":
    break

  str_input = str_input.replace(",", "").replace(".", "").replace(";", "").replace("!", "").replace("?", "")

  str_input = str_input.upper()

  print(str_input)

print("Bye!")
 
