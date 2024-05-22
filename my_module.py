internal_value = 42

from arithmetic_list_operations import math_op, list_operations
from string_geometry_operations import string_operations, geometry_operations

# Проверка арифметических операций
print(math_op.addition(5, 3))
print(math_op.subtraction(10, 4))
print(math_op.multiplication(7, 2))

# Проверка операций над списками
my_list = [1, 2, 3, 4, 2, 4, 5]
print(list_operations.is_element_present(my_list, 3))
print(list_operations.count_element_frequency(my_list, 2))

# Проверка строковых операций
my_string = "level"
print(string_operations.is_palindrome(my_string))
print(string_operations.calculate_string_length(my_string))
print(string_operations.convert_to_lower_case(my_string))

# Проверка геометрических операций
print(geometry_operations.calculate_circle_area(5))
print(geometry_operations.calculate_rectangle_area(4, 6))
print(geometry_operations.calculate_triangle_area(3, 4))
