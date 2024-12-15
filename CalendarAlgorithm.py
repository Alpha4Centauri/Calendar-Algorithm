month = input("Enter the month: ")

day = int(input("Enter the date: "))

year = int(input("Enter the year: "))

print()

def currentYear():
  dayCode = {1: "Sunday", 2: "Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"} 

  firstDays = [6, 2, 2, 5, 7, 3, 5, 1, 4, 6, 2, 4]

  monthCode = {"January":1, "February":2, "March":3, "April":4, "May": 5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

  firstDayCodePosition = monthCode[month]

  firstDayCodeActual = firstDays[firstDayCodePosition - 1]

  remainder = day % 7

  actualDate = (firstDayCodeActual + remainder) - 1

  if actualDate > 7:
    actualDate = actualDate % 7

  print(str(month), str(day) + ",", str(year), "is a", dayCode[actualDate] + "!")

def currentCenturyFuture():
  years = []

  for i in range(1, year - 2021):
    years.append(i)

  print(years)

  dayCode = {1: "Sunday", 2: "Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"} 

  firstDays = [6, 2, 2, 5, 7, 3, 5, 1, 4, 6, 2, 4]

  for j in years:
    for i in range(len(firstDays)):
      if (2021 + j) % 4 != 0 and year > 2022:
        firstDays[i] = firstDays[i] + 1
        if firstDays[i] > 7:
          firstDays[i] = firstDays[i] % 7
      if (2021 + j) % 4 == 0:
        firstDays[i] = firstDays[i] + 2
        if firstDays[i] > 7:
          firstDays[i] = firstDays[i] % 7

  print(firstDays)
    

  monthCode = {"January":1, "February":2, "March":3, "April":4, "May": 5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

  firstDayCodePosition = monthCode[month]

  firstDayCodeActual = firstDays[firstDayCodePosition - 1]

  remainder = day % 7

  actualDate = (firstDayCodeActual + remainder) 

  if actualDate > 7:
    actualDate = actualDate % 7

  print(str(month), str(day) + ",", str(year), "is a", dayCode[actualDate] + "!")

def futureCenturies():
  years = []
  centuries = []
   
  for i in range(1, year - 2021):
    years.append(i)

  for i in range(1, year - 2021):
    if i % 100 == 0:
      centuries.append(i/100)

  print(years)

  print(centuries)

  dayCode = {1: "Sunday", 2: "Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"} 

  firstDays = [6, 2, 2, 5, 7, 3, 5, 1, 4, 6, 2, 4]

  for j in years:
    for i in range(len(firstDays)):
      if (2021 + j) % 4 != 0 and j % 100 != 0:
        firstDays[i] = firstDays[i] + 1
        if firstDays[i] > 7:
          firstDays[i] = firstDays[i] % 7
      if (2021 + j) % 4 == 0 and j % 100 != 0:
        firstDays[i] = firstDays[i] + 2
        if firstDays[i] > 7:
          firstDays[i] = firstDays[i] % 7

      if (2021 + j) % 4 != 0 and j % 100 == 0:
        for k in centuries:
          firstDays[i] = firstDays[i] - k
          if firstDays[i] > 7:
            firstDays[i] = firstDays[i] % 7
      if (2021 + j) % 4 == 0 and j % 100 == 0:
        for k in centuries:
          firstDays[i] = (firstDays[i] + 1) - k
          if firstDays[i] > 7:
            firstDays[i] = firstDays[i] % 7

  print(firstDays)
    

  monthCode = {"January":1, "February":2, "March":3, "April":4, "May": 5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}

  firstDayCodePosition = monthCode[month]

  firstDayCodeActual = firstDays[firstDayCodePosition - 1]

  remainder = day % 7

  actualDate = (firstDayCodeActual + remainder) 

  if actualDate > 7:
    actualDate = actualDate % 7

  print(str(month), str(day) + ",", str(year), "is a", dayCode[actualDate] + "!")
  

def pastYears():
  pass
if year == 2021:
  currentYear()

if year > 2021 and year < 2121:
  currentCenturyFuture()

if year > 2121:
  futureCenturies()

if year < 2021:
  pastYears()

# Error Case 1:

# Sample: December 20, 2021 should be Monday

# Current Algorithm Fix:

# 20 % 7 = 6 ; firstDayCodeActual = 4; 6 + 4 = 10 - 1 = 9 % 7 = 2

# Error Case 2 (every 100 years):

# Sample: July 8 (future)

# 2121 = 1 day off; 2221 = 2 days; 2321 = 3 days; 2421 = 3 days; 2521 = 5 days; 2621 = 6 days; 2721 = 1 day behind

  
# Logic:

# Sample Input: June 17, 2021

# 17 = date, startDate = Tuesday

# 17 % 7 = 3

# Tuesday = 3; 3 + 3 = 6 - 1 = Thursday