import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passcharacters = []
i = nr_letters
while i > 0:
    index = random.randint(0,len(letters)-1)
    passcharacters.append(letters[index])
    i = i -1
j = nr_symbols
while j > 0:
    index = random.randint(0,len(symbols)-1)
    passcharacters.append(symbols[index])
    j = j -1
k = nr_numbers
while k > 0:
    index = random.randint(0,len(numbers)-1)
    passcharacters.append(numbers[index])
    k = k -1


random.shuffle(passcharacters)
s = ''
password = s.join(passcharacters)
print(password)