from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "J J", "birthday": "1989.01.18"}
]

def weekend_days(date_birthday):
    if datetime.isoweekday(date_birthday) == 6:
        new_date = date_birthday + timedelta(days=2)
    elif datetime.isoweekday(date_birthday) == 7:
         new_date = date_birthday + timedelta(days=1) 
    else:
        new_date = date_birthday
    return new_date   

def get_upcoming_birthdays(users):
    for user in users:
        date_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        date_today    = datetime.strptime("2024.01.22", "%Y.%m.%d").date()
        # date_today    = datetime.today().date()

        birthday_this_year = datetime(date_today.year, date_birthday.month, date_birthday.day).date()

        if birthday_this_year < date_today:
            new_birthday = datetime(date_today.year + 1, date_birthday.month, date_birthday.day).date()
            new_birthday = weekend_days(new_birthday)
            user.clear() # Питання як прибрати пусті словники зі списку?    
        else:
            difference_days = (birthday_this_year - date_today).days
            if difference_days <= 7:
                birthday_this_year = weekend_days(birthday_this_year)
                birthday_this_year = birthday_this_year.strftime("%Y-%m-%d")

                user["congratulation_date"] = user.pop("birthday")
                user.update({"name":user["name"], "congratulation_date":birthday_this_year})
   
    return users

print(get_upcoming_birthdays(users))