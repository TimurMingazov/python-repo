numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
first_half = numbers[:4] #Берем числа до пропущенного
second_half = numbers[5:] #Числа после пропущенного
numbers_without_none = first_half + second_half # Список чисел без пропущенного
sum_of_numbers = sum(numbers_without_none) #Сумма чисел без пропущенного
count_of_numbers = len(numbers) #Кол-во цифры, считая пропущенное
average_of_numbers = sum_of_numbers / count_of_numbers #Среднее значение
numbers[4] = average_of_numbers

print("Измененный список:", numbers)
