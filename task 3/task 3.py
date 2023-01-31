# Задание 3.

# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
n = int(input("Введите число > "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print(f"Сумма чисел n + nn + nnn > {total}")