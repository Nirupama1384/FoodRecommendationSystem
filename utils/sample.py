import csv,random

file = open('db\orders.csv', 'r')
read_obj = csv.reader(file)
d = {}
skip = 1
for row in read_obj:
    if skip == 1:
        skip = 0
        continue
    if row[2] not in d:
        d[row[2]] = 1
    else:
        d[row[2]] += 1
file.close()
print(d)
"""
file = open('../db/food.csv', 'r')
read_obj = csv.reader(file)
food = []
skip = 1
for row in read_obj:
    if skip == 1:
        skip = 0
        food.append(row)
        continue
    row[4] = d[row[0]]
    food.append(row)
file.close()

file = open('../db/food_new.csv', 'w')
write_obj = csv.writer(file)
write_obj.writerows(food)
file.close()"""
"""
file = open("../db/food_new.csv","r")
food = csv.reader(file)
food_list = []
skip = 1
for row in food:
    if skip == 1:
        skip = 0
        continue
    if(len(row) != 9):
        print(len(row),row)
    food_list.append(row)
file.close()"""
# print(food_list)
