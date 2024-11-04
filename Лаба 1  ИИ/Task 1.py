numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index_none = numbers.index(None)
numbers[index_none] = 0

sum_num = sum(numbers)
count_num = len(numbers)

numbers[index_none] = sum_num / count_num

print("Измененный список:", numbers)
