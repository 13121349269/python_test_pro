from random import randint

def roll_dice(n=20):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1,6)
    return total

def add(a=0,b=0,c=0):
    """三个数相加"""
    return a+b+c
print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1,2))
print(add(1,2,3))
print(add(a=10,c=20,b=5))

"""n个参数 可变参数"""
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

"""计算最大公约数和最小公倍数"""
def gcd(x,y):
    """最大公约数"""
    (x,y) = (y,x) if x >y else(x,y)
    for factor in range(x,0,-10):
        if x % factor == 0 and y % factor ==0:
            return factor
def lcm(x,y):
    """最小公倍数"""
    return  x*y // gcd(x,y)

"""判断回文数"""
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        #每一位数字都循环
        total = total * 10 + temp % 10
        temp //= 10
    return total == num
"""
判断一个数是否是素数
"""
def is_prime(num):
    for factor in range(2,int(num ** 0.5) + 1):
        print(factor)
        if num % factor == 0:
            return False
    return True if num != 1 else False
"""
判断输入的正整数是不是回文素数
"""
if __name__ == '__main__':
    num = int(input("输入"))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)