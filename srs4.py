#1
def replace_quotes(string):
	result = ''
	for char in string:
    	if char == '"':
        	result += "'"
    	elif char == "'":
        	result += '"'
    	else:
        	result += char
	return result


#2
def is_palindrome(string):
	if not isinstance(string, str):
    	raise ValueError("Input must be a string")


	cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
	return cleaned_string == cleaned_string[::-1]


#3
def custom_split(string, separator=None):
    if not isinstance(string, str):
        raise ValueError("Input must be a string")

    if separator is None:
        separator = ' '

    result = []
    word = ""
    for char in string:
        if char != separator:
            word += char
        elif word:
            result.append(word)
            word = ""

    if word:
        result.append(word)

    return result

#4
from typing import List

def split_by_index(string: str, indexes: List[int]) -> List[str]:
	if not isinstance(string, str):
    	raise ValueError("Input string must be a string")

	if not isinstance(indexes, list):
    	raise ValueError("Indexes must be a list")

	result = []
	prev_index = 0

	for index in indexes:
    	if isinstance(index, int) and index > prev_index:
        	result.append(string[prev_index:index])
        	prev_index = index

	result.append(string[prev_index:])
	return result

#5
from typing import Tuple

def get_digits(*args: int) -> Tuple[int]:
	digits = []

	for num in args:
    	if not isinstance(num, int):
        	raise ValueError("All arguments must be integers")

    	digits.extend(int(digit) for digit in str(num))

	return tuple(digits)

#6
def get_longest_word(s: str) -> str:
	if not isinstance(s, str):
    	raise ValueError("Input must be a string")

	words = s.split()
	longest_word = ''

	for word in words:
    	# Видалення будь-яких спеціальних символів зі слова
    	cleaned_word = ''.join(char for char in word if char.isalnum())

    	if len(cleaned_word) > len(longest_word):
        	longest_word = cleaned_word

	return longest_word

#7
from typing import List

def foo(nums: List[int]) -> List[int]:
	if not isinstance(nums, list) or not all(isinstance(num, int) for num in nums):
    	raise ValueError("Input must be a list of integers")

	total_product = 1
	zero_count = 0

	for num in nums:
    	if num == 0:
        	zero_count += 1
    	else:
        	total_product *= num

	result = []
	for num in nums:
    	if zero_count > 1 or (zero_count == 1 and num != 0):
        	result.append(0)
    	elif zero_count == 1 and num == 0:
        	result.append(total_product)
    	else:
        	result.append(total_product // num)

	return result

#8
from typing import List, Optional, Union

def get_pairs(elements: List[Union[int, str]]) -> Optional[List[tuple]]:
	if len(elements) <= 1:
    	return None

	pairs = []
	for i in range(len(elements) - 1):
    	pair = (elements[i], elements[i + 1])
    	pairs.append(pair)

	return pairs

#9
def sum_of_odd_digits(n: int) -> int:
	if not isinstance(n, int) or n < 0:
    	raise TypeError("n should be a non-negative integer")

	sum_odd = 0
	for digit in str(n):
    	if int(digit) % 2 != 0:
        	sum_odd += int(digit)

	return sum_odd

#10

def sum_binary_1(n: int) -> int:
	if not isinstance(n, int) or n < 0:
    	raise TypeError("n should be a non-negative integer")

	binary = bin(n)[2:]  # отримуємо двійкове представлення числа n без префіксу "0b"
	sum_ones = binary.count('1')  # підрахунок кількості одиниць у двійковому представленні

	return sum_ones

#11
def fibonacci_loop(seq):
    fib_seq = []
    for num in seq:
        if isinstance(num, str):
            break
        elif isinstance(num, float):
            continue
        elif isinstance(num, int):
            a, b = 0, 1
            fib_num = []
            while a <= num:
                if a % 2 != 0:
                    fib_num.append(a)
            a, b = b, a + b
            fib_seq.extend(fib_num)

    print(' '.join(str(num) for num in fib_seq))



