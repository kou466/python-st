# create module

PI = 3.141592

def number_input():
    output = input("숫자를 입력해주세요: ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius
