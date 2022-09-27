# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print("Type the quarter's number: ")
quarter_num = int(input())

if quarter_num == 1:
    print(" X > 0 and Y > 0")
elif quarter_num == 2:
    print(" X < 0 and Y > 0")
elif quarter_num == 3:
    print(" X < 0 and Y < 0")
elif quarter_num == 4:
    print(" X > 0 and Y < 0")
elif quarter_num < 1 or quarter_num > 4:
    print("Incorrect number. There are only four quarters.")