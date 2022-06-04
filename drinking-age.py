def people_with_age_drink(age):
    if age < 14:
        return "Drink Toddy"
    elif age < 18:
        return "Drink Coke"
    elif age < 21:
        return "Drink Beer"
    elif age >= 21:
        return "Drink Whiskey"
print(people_with_age_drink(24))