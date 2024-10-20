import json

with open("orders_july_2023.json", "r") as my_file:
    orders_july = my_file.read()
orders = json.loads(orders_july)
print(orders)
print(type(orders))

#1
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'1. Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

#2
max_quantity = 0
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    max_quantity_order = {}
    max_quantity_order[max_order] = max_quantity
    if quantity > max_quantity:
        max_order = order_num
        max_quantity = quantity
print(f'2. Номер заказа с самым большим колличеством товаров: {max_quantity_order}, количество товаров: {max_quantity}' )

#3
date_dict = {}
for order_num, order_data, in orders.items():
    date = order_data['date']
    date_dict[date] = date_dict.get(date, 0) + 1

for date in sorted(date_dict):
    max_value = max(date_dict.values())
    if date_dict[date] ==max_value:
        print(f'3. Больше всего сделано заказов {date}: {date_dict[date]}')

#4
max_orders, user_dict = 0, {}
for order_num, order_data, in orders.items():
    user_id = order_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + 1
    orders_2 = user_dict.get(user_id)
    if orders_2 > max_orders:
        max_orders = orders_2
print(f'4. Самое большое количество заказов сделал пользователь под номером: {user_id}, количество заказов {max_orders}')

#5
user_dict, max_price = {}, 0
for  order_num, order_data, in orders.items():
    user_id = orders_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + orders_data['price']
    all_price = user_dict.get(user_id)
    if all_price > max_price:
        max_price = all_price
print(f'5. Пользователь {user_id} имеет самую большую суммарную стоимость заказов за июль: {max_price}')

#6
sum_price, count = 0, 0
for order_num, orders_data in orders.items():
    sum_price += orders_data['price']
    count = len(orders)
print(f'6. Средняя стоимость заказа в июле: {sum_price//count}')

#7
sum_all, count = 0, 0
for order, data in orders.items():
    sum_all += data['price']
    count += data['quantity']
print(f'7. Средняя стоимость товаров в июле: {sum_all/count}')