## Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).


print('Type a number for X: ')
user_x = int(input())

print('Type a number for Y: ')
user_y = int(input())

if user_x == 0 and user_y == 0:
    print(' Input a number bigger or smaller than 0')
elif user_x > 0 and user_y > 0:
    print(f" Your point is in the first quarter ({user_x}, {user_y})")
elif user_x < 0 and user_y > 0:
    print(f" Your point is in the second quarter ({user_x}, {user_y})")
elif user_x < 0 and user_y < 0:
    print(f" Your point is in the third quarter ({user_x}, {user_y})")
elif user_x > 0 and user_y < 0:
    print(f" Your point is in the fourth quarter ({user_x}, {user_y})")
elif user_x == 0:
    print(f" Your point is on the y-axis ({user_x}, {user_y})")
elif user_y == 0:
    print(f" Your point is on the x-axis ({user_x}, {user_y})")