customers = 0
cheap = 0
medium = 0
expensive = 0
sales = 0

more = 'yes'

while more == 'yes':
    customers += 1
    print('Customer', customers)

    more = input('Another customer? yes/no')

print('Customers served:', customers)