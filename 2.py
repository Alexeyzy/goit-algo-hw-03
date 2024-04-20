import random

GO_FUNCTION = True

try:
    min      = int(input("Введіть мінімальне число не менше 1:"))
    max      = int(input("Введіть максимальне число не більше 1000:"))
    quantity = int(input("Введіть кількість чисел які треба вибрати:"))
except ValueError:
    print("Введіть тільки цифри")
    GO_FUNCTION = False
else:
    if min < 1 or min > max:
        print("min менше 1 або більше max") 
        GO_FUNCTION = False      
    elif max > 1000 or max < min:
        print("max білш 1000 або менше min")
        GO_FUNCTION = False
    elif len(range(min, max + 1)) < quantity:
        print("quantity не входить в діапозон між min та max")
        GO_FUNCTION = False

def get_numbers_ticket(min, max, quantity):         
    mass = set()
    while len(mass) < quantity:
        mass.add(random.randint(min,max))
    return  sorted(mass) 

if GO_FUNCTION:
    print(get_numbers_ticket(min, max, quantity))
else:
    print("Повторіть введення")    