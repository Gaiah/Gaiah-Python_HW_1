## Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print('Type a number between 1 and 7: ')
user_num = int(input())
user_num = abs(user_num)

if user_num > 0 and user_num < 6:
    print('Weekday')
elif user_num == 6 or user_num == 7:
    print('Weekend')
else:
    print('Incorrect number')

