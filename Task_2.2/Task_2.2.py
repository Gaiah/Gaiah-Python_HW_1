
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from dis import dis


print("Input A_x: ")
a_x = int(input())

print("Input A_y: ")
a_y = int(input())

print("Input B_x: ")
b_x = int(input())

print("Input B_y: ")
b_y = int(input())

distance = (((a_x - b_x) **2) + ((a_y - b_y) **2)) ** (0.5)
print(f'The distance between Your points = {round(distance, 2)}')

