# Написать скрипт который проходится по ключам и проверяет значения
# a) Если значение делиться на 3, то записываем строку “Hi”
# b) Если значение делиться на 5, то записываем строку “Bye”

# ПРИМЕР:
# Дано -> dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# Результат -> a = Bye
# b = Hi
dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
a=dict1.values()
for i in a:
	if i%3==0:
		print('b=Hi')
	elif i%5==0:
		print('a=Bye')