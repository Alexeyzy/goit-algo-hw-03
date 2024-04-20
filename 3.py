import re

phone_number = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451++234",
    "(050)8+++88+++9900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(number):

    number = re.sub("[^0-9+]","",number)
       
    while number.find("+",1) != -1:
        li = list(number)
        li[number.find("+",1)] = ""
        number = "".join(li)

    if number[0] != "+":  
        number = "+" + number      
    if number[1] != "3":
        number = number[:1] + "3" + number[1:]
    if number[2] != "8":  
        number = number[:2] + "8" + number[2:]

    return number

sanitized_numbers = [normalize_phone(number) for number in phone_number]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)