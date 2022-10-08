# a = int(input('Enter num1:'))
# b = int(input('Enter num2:'))
# print(a+b)
# age = int(input('Enter Age:'))
# if age < 18:
#     print('a gift')
# if age >= 18 and age <= 20:
#     print('a gift')
#     print('a task')
# if age > 20:
#     print('ghkgk')
a = int(input('Enter num1:'))
b = int(input('Enter num2:'))
c = int(input('Enter num3:'))
if a > b:
    if b > c:
        print('a is maximum')
elif a < c:
    if c > b:
        print('c is maximum')
else:
    print('b is maximum')
