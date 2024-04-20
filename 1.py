from datetime import datetime

date = input("Введіть дату в форматі РРРР-ММ-ДД:")

def get_days_from_today(date):
   
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
    except Exception as date_object:
        return "Не коректне введення дати"
    else:
        res = datetime.today() - date_object
        return res.days

print(get_days_from_today(date))