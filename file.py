city=['NewYork']
for i in range(10):
	print('''Список городов:
	1. Нью Йорк
	Выберите действие:
	1. Добавить новый город
	2. Отобразить список городов
	3. Заменить город
	4. Удалить город
	5. Посетить следующий город
		6. Выход''')
	x=int(input('Введите команду'))
	if x==1:
		print(city.append('Brooklyn'))
	
