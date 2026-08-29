from Function_Folder1.myfunctions01 import calculate_area_of_triangle, print_colored_message

print_colored_message('Hello World', 'green')

a=5
b=4
c=3
Area = calculate_area_of_triangle(a, b, c)
print(f'The area of the triangle is: {Area}')

print_colored_message(f'The area of the triangle is: {Area}', 'blue')
