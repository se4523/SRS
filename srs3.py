num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, /, *, mod, pow, div): ")

result = None

if operation == "+":
	result = num1 + num2
elif operation == "-":
	result = num1 - num2
elif operation == "*":
	result = num1 * num2
elif operation == "/":
	if num2 == 0:
    	print("Ділення на 0!")
	else:
    	result = num1 / num2
elif operation == "mod":
	if num2 == 0:
    	print("Ділення на 0!")
	else:
    	result = num1 % num2
elif operation == "pow":
	result = num1 ** num2
elif operation == "div":
	if num2 == 0:
    	print("Ділення на 0!")
	else:
    	result = num1 // num2
else:
	print("Непідтримувана операція!")

if result is not None:
	print("Результат:", result)


#2

n = int(input("Введіть кількість програмістів: "))


if n == 1:
	ending = ""
elif 2 <= n <= 4:
	ending = "а"
else:
	ending = "ів"
result = f"{n} програміст{ending}"
print(result)

#3
ticket_number = input("Введіть номер квитка (шість цифр): ")
if len(ticket_number) != 6:
	print("Некоректний номер квитка")
else:

	digits = [int(digit) for digit in ticket_number]
	first_sum = sum(digits[:3])
	last_sum = sum(digits[3:])
	if first_sum == last_sum:
    	print("Щасливий")
	else:
    	print("Звичайний")

#4
x1, y1, x2, y2 = map(int, input("Введіть координати двох клітин шахової дошки (x1 y1 x2 y2): ").split())

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
	print("YES")
else:
	print("NO")

#5
N, M, x, y = map(int, input("Введіть розміри басейну та відстані до бортиків (N M x y): ").split())

min_distance = min(x, y, N - x, M - y)

print("Мінімальна відстань до борту:", min_distance)


