month = input("Enter the month: ")
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))

print()
dayCode = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
firstDays = [6, 2, 2, 5, 7, 3, 5, 1, 4, 6, 2, 4]
monthLength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthCode = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def currentYear():
    global month, day, year 
    firstDayCodePosition = monthCode[month]
    firstDayCodeActual = firstDays[firstDayCodePosition - 1]
    remainder = day % 7
    actualDate = (firstDayCodeActual + (remainder - 1)) % 7

    if actualDate == 0:
        actualDate = 7

    if day >= 1 and day <= monthLength[firstDayCodePosition - 1]: 
        print(f"{month} {day}, {year} is a {dayCode[actualDate]}!")
    else:
        if is_leap_year(year) and day >= 1 and day <= 29:
            print(f"{month} {day}, {year} is a {dayCode[actualDate]}!")
        else:
            print("Invalid date, please try again.")

def previousYears():
    global month, day, year

    for i in range(2020, year - 1, -1):
        if is_leap_year(i + 1): 
            for j in range(2, len(firstDays)):
                firstDays[j] -= 2
            firstDays[0] = abs((firstDays[0] - 1) % 7)
            if firstDays[0] == 0:
                firstDays[0] = 7
            firstDays[1] = abs((firstDays[1] - 1) % 7)
            if firstDays[1] == 0:
                firstDays[1] = 7
        elif is_leap_year(i):  
            firstDays[0] -= 2
            firstDays[1] -= 2
            for j in range(2, len(firstDays)):
                firstDays[j] = abs((firstDays[j] - 1) % 7)
                if firstDays[j] == 0:
                    firstDays[j] = 7
        else: 
            for j in range(2, len(firstDays)):
                firstDays[j] = abs((firstDays[j] - 1) % 7)
                if firstDays[j] == 0:
                    firstDays[j] = 7
            firstDays[0] = abs((firstDays[0] - 1) % 7)
            if firstDays[0] == 0:
                firstDays[0] = 7
            firstDays[1] = abs((firstDays[1] - 1) % 7)
            if firstDays[1] == 0:
                firstDays[1] = 7

    firstDayCodePosition = monthCode[month]
    firstDayCodeActual = firstDays[firstDayCodePosition - 1]
    remainder = day % 7
    actualDate = (firstDayCodeActual + (remainder - 1)) % 7

    if actualDate == 0:
        actualDate = 7

    if day >= 1 and day <= monthLength[firstDayCodePosition - 1]: 
        print(f"{month} {day}, {year} is a {dayCode[actualDate]}!")
    else:
        if is_leap_year(year) and day >= 1 and day <= 29:
            print(f"{month} {day}, {year} is a {dayCode[actualDate]}!")
        else:
            print("Invalid date, please try again.")

def futureYears():
    global month, day, year

    for i in range(2022, year + 1, 1):
        if is_leap_year(i): 
            for j in range(2, len(firstDays)):
                firstDays[j] += 2
            firstDays[0] = (firstDays[0] + 1) % 7
            if firstDays[0] == 0:
                firstDays[0] = 7
            firstDays[1] = (firstDays[1] + 1) % 7
            if firstDays[1] == 0:
                firstDays[1] = 7
        elif is_leap_year(i - 1):  
            firstDays[0] += 2
            firstDays[1] += 2
            for j in range(2, len(firstDays)):
                firstDays[j] = (firstDays[j] + 1) % 7
                if firstDays[j] == 0:
                    firstDays[j] = 7
        else: 
            for j in range(2, len(firstDays)):
                firstDays[j] = (firstDays[j] + 1) % 7
                if firstDays[j] == 0:
                    firstDays[j] = 7
            firstDays[0] = (firstDays[0] + 1) % 7
            if firstDays[0] == 0:
                firstDays[0] = 7
            firstDays[1] = (firstDays[1] + 1) % 7
            if firstDays[1] == 0:
                firstDays[1] = 7

    firstDayCodePosition = monthCode[month]
    firstDayCodeActual = firstDays[firstDayCodePosition - 1]
    remainder = day % 7
    actualDate = (firstDayCodeActual + (remainder - 1)) % 7

    if actualDate == 0:
        actualDate = 7

    if day >= 1 and day <= monthLength[firstDayCodePosition - 1]: 
        print(f"{month} {day}, {year} is a {dayCode[actualDate]}!")
    else:
        if is_leap_year(year) and day >= 1 and day <= 29:
            print(f"{month} {day}, {year} is a {dayCode[actualDate]}!")
        else:
            print("Invalid date, please try again.")


if year < 2021:
    previousYears()
    
elif year == 2021:
    currentYear()

elif year > 2021:
    futureYears()
