def create_report(data, func):
   revenue, quantity = func(data, revenue=True, quantity=True)
   report = f"Средний доход за данный период составил {revenue/len(data)}.\n"
   report += "Количество проданных единиц каждого товара:\n"
   for item, qty in quantity.items():
       report += f"{item}: {qty}\n"
   return report