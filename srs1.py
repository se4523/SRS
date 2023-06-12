#2
def distribute_apples(n, k):
	apples_per_student = k // n
	remaining_apples = k % n
	return apples_per_student, remaining_apples


# Введення кількості школярів (n) і кількості яблук (k)
n = int(input("Введіть кількість школярів: "))
k = int(input("Введіть кількість яблук: "))

# Розподіл яблук і виведення результату
apples_per_student, remaining_apples = distribute_apples(n, k)
print("Кількість яблук, що дістається кожному школяру:", apples_per_student)
print("Кількість яблук, що залишається у кошику:", remaining_apples)

#3
def calculate_alarm_time(sleep_duration, sleep_hour, sleep_minute):
	total_sleep_minutes = sleep_hour * 60 + sleep_minute
	wake_up_minutes = total_sleep_minutes + sleep_duration
	alarm_hour = wake_up_minutes // 60
	alarm_minute = wake_up_minutes % 60

	return alarm_hour, alarm_minute
sleep_duration = int(input("Введіть тривалість сну (в хвилинах): "))
sleep_hour = int(input("Введіть годину лягання: "))
sleep_minute = int(input("Введіть хвилину лягання: "))

alarm_hour, alarm_minute = calculate_alarm_time(sleep_duration, sleep_hour, sleep_minute)
print("Час будильника:")
print(alarm_hour)
print(alarm_minute)


# 4
# Введення кількості учнів у кожному з трьох класів
class1_students = int(input("Кількість учнів у класі 1: "))
class2_students = int(input("Кількість учнів у класі 2: "))
class3_students = int(input("Кількість учнів у класі 3: "))

# Розрахунок кількості партою та виведення результату
desks_class1 = (class1_students + 1) // 2  # Кількість партою для класу 1
desks_class2 = (class2_students + 1) // 2  # Кількість партою для класу 2
desks_class3 = (class3_students + 1) // 2  # Кількість партою для класу 3

total_desks = desks_class1 + desks_class2 + desks_class3  # Загальна кількість партою

print("Загальна кількість партою, яку потрібно закупити:", total_desks)


#5
# Введення трьох цілих чисел
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
num3 = int(input("Введіть третє число: "))

# Знаходження максимального числа
max_num = (num1 + num2 + abs(num1 - num2)) // 2
max_num = (max_num + num3 + abs(max_num - num3)) // 2

# Знаходження мінімального числа
min_num = (num1 + num2 - abs(num1 - num2)) // 2
min_num = (min_num + num3 - abs(min_num - num3)) // 2

# Знаходження числа, що залишилося
remaining_num = num1 + num2 + num3 - max_num - min_num

# Виведення результату
print(max_num)
print(min_num)
print(remaining_num)
