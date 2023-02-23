##Узнайте у пользователя целое положительное число n.
##Найдите сумму чисел n + nn + nnn.

a = int(input("Введите число:"))
total = (a + int(str(a) + str(a)) + int(str(a) + str(a)+ str(a)))
print("Сумма чисел n + nn + nnn - %d" % total)
