import csv,random
file = open('order.csv', 'r')
obj = csv.reader(file)
# print(obj.read())
rows = []
user_id = [x for x in range(1,17)]
order_id = 117
# print(user_id)
# next(obj)
count = 0
for row in obj:
    # print(row)
    if(count == 0):
        rows.append(row)
        count += 1
        continue
    else:
        # print("Length ",len(row))
        row[1] = str(random.randint(1,16))
        rows.append(row)
# print(rows)
file.close()
# rows = []
# rows = rows*3
f = open("./db/food.csv", "r")
food = csv.reader(f)
food_list = []
skip = 1
for row in food:
    if(skip == 1):
        skip = 0
        continue
    food_list.append([row[0],row[3]])
for order_id in range(117,1000000):
    food_rand = random.randint(0,len(food_list)-1)
    user_id_rand = random.randint(1,16)
    rows.append([str(order_id),str(user_id_rand),food_list[food_rand][0],"1","2019-06-29 9:26:00","served",food_list[food_rand][1]])
f.close()
# print(food_list)



file =open('orders.csv', 'w')
writer = csv.writer(file)
writer.writerows(rows)
file.close()