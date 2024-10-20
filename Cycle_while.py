num = int(input('Введите число: '))
data = []
while num != 0:
    data.append(num)
    num = int(input('Введите число: '))
data.sort()
print(data)
