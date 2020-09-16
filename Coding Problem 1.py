# Tri Dao
# 1954347

# Calculate the age of person based on current date und the birthday of the user.

from datetime import date

def calculateAge(currentDate, birthDate):
    today = currentDate
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

print("Birthday Calculator")
print('Current day')
mm1 = int(input('Month: '))
dd1 = int(input('Day: '))
yy1 = int(input('Year: '))

print('Birthday')
mm2 = int(input('Month: '))
dd2 = int(input('Day: '))
yy2 = int(input('Year: '))

print("You are", calculateAge(date(yy1, mm1, dd1), date(yy2, mm2, dd2)), "years old.")

if (dd1 == dd2):
    print("Happy Birthday!")
