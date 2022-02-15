"""
1-100 求和
range(101) 0-100的整数
range(1, 101) 1-100的整数
range(1,101,2)1-100的奇数，2是步长
range(100,0,-2) 100-1的偶数，-2是步长
"""
sum = 0
for x in range(101):
    sum += x
print(sum)

"""
1-100偶数求和
"""
sum = 0
for x in range(2, 101,2):
    sum += x
print(sum)

"""
分支结构 1-100偶数求和
"""
sum = 0
for x in range(1,101):
    if x % 2 == 0:
        sum += x
print(sum)

"""
while 循环，猜数字游戏
"""
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input("输入： "))
    print(type(number),type(answer))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜')
        break
print('共猜了 %d次' % counter)
if counter > 7:
    print('IQ不足')

"""
99 乘法表
"""
for n in range(1, 10):
    for j in range(1, n + 1):
        print('%d*%d=%d' % (n, j, n*j), end='\t')
    print()

"""
输入整数判断是不是素数 (素数：只能被1和自身整除的大于1的整数)
"""
from math import sqrt

num = int(input("输入一个正整数"))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d 是素数' % num)
else:
    print('%d不是素数' % num)

"""
两个正整数，计算最大公约数和最小公倍数 (最大公约数：两个数的公共因子中最大的那个数。最小公倍数：同时被两个数整除的最小的那个数)
"""
x = int(input('x= '))
y = int(input('y= '))
#如果x大于y 就交换x和y的值
if x > y:
    x, y = y, x
#从两个数中较小的数开始做递减
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d 和%d 的最大公约数是%d' % (x, y, factor))
        print('%d 和 %d的最小公倍数是 %d ' % (x,y, x*y // factor))
        break

"""                             
打印三角形                           
"""
row = int(input("输入行数"))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print(end='\n')

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ',end='')
        else:
            print('*',end='')
    print('')

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()