# Tri Dao
# 1954347
# Automobile service invoice

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

def services_Cost(x):
    if x == "Oil change":
        return 35
    if x == "Tire rotation":
        return 19
    if x == "Car wash":
        return 7
    if x == "Car wax":
        return 12

Services1 = input("Select first service:\n")
Services2 = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")

if 'Oil change' in Services1:
    print('Service 1: {}, ${}'.format(Services1, services_Cost(Services1)))
    Services1 = 35
elif 'Tire rotation' in Services1:
    print('Service 1: {}, ${}'.format(Services1, services_Cost(Services1)))
    Services1 = 19
elif 'Car wash' in Services1:
    print('Service 1: {}, ${}'.format(Services1, services_Cost(Services1)))
    Services1 = 7
elif 'Car wax' in Services1:
    print('Service 1: {}, ${}'.format(Services1, services_Cost(Services1)))
    Services1 = 12
else:
    print('Service 1:','No service')
    Services1 = 0


if 'Oil change' in Services2:
    print('Service 2: {}, ${}'.format(Services2, services_Cost(Services2)))
    Services2 = 35
elif 'Tire rotation' in Services2:
    print('Service 2: {}, ${}'.format(Services2, services_Cost(Services2)))
    Services2 = 19
elif 'Car wash' in Services2:
    print('Service 2: {}, ${}'.format(Services2, services_Cost(Services2)))
    Services2 = 7
elif 'Car wax' in Services2:
    print('Service 2: {}, ${}'.format(Services2, services_Cost(Services2)))
    Services2 = 12
else:
    print('Service 2:','No service')
    Services2 = 0

print('\nTotal: ${}'.format(Services1 + Services2))