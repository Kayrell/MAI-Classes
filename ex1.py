from math import sin

x = float(input())
y = float(input())

# ToDo - a
if x ** 2 + y ** 2 > 4 and y < x and x < 2:
    print("точка входит в область")
else:
    print('точка не входит в область')

# ToDo - б
if y < sin(x) and y < 0.5 and y > 0:
    print('точка входит в область')
else:
    print('точка не входит в область')