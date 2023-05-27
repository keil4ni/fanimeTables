# program that sorts all table numbers i input so i can visit them in order when i go to fanime Lol
# does not check for invalid inputs

table_list = list()
table = int(input('enter table number, enter 000 to quit: '))
table_list.append(table)

while table != 000:
    print('table', table, 'has been added to list')
    table = int(input('enter table number, enter 000 to quit: '))
    table_list.append(table)

print('\nyou have broken out of the while loop. list will now be sorted')
table_list.pop() # removes 000 value from the list
table_list.sort()
print(table_list, '\nhave fun at fanime!')