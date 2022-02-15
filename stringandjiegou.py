import sys

s1 = 'hello ' *3
print(s1)

s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)

str2 = 'abc123456'
print(str2[2])
print(str2[2:5])
print(str2[2:])
print(str2[2::2])
print(str2[::2])
print(str2[::-1])
print(str2[-3:-1])

str1 = 'hello,world!'
print(len(str1))
#字符串首字母大写的拷贝
print(str1.capitalize())
#获得字符串每个单词首字母大写的拷贝
print(str1.title())
#字符串全部大写的拷贝
print(str1.upper())
#从字符串中查找子串所在的位置
print(str1.find('or'))
print(str1.find('shit'))
#与find类似但找不到子串时会报错
print(str1.index('or'))
#print(str1.index('shit'))
#检查字符串是否以指定的字符串开头
print(str1.startswith('He'))
print(str1.startswith('hel'))
#以安插字符串是否以指定的字符串结尾
print(str1.endswith('!'))
#将字符串以指定的宽度居中并在两侧填充指定的字符 ***hello,world!***
print(str1.center(50,'*'))
#将字符串以指定的宽度靠右防止左侧填充指定的字符 *****hello,world
print(str1.rjust(50,'*'))
str2 = 'abc123456'
#检查字符串是否由数字构成
print(str2.isdigit())
#检查字符串是否以字母构成
print(str2.isalpha())
#检查字符串是否以数字和字母构成
print(str2.isalnum())
str3 = '   jackfrued@126.com '
print(str3)
#获得字符串修建左右两侧空格之后的拷贝
print(str3.strip())

#格式化输出字符串
a, b = 5,10
print('%d * %d = %d' % (a,b,a *b))
#格式化方式2
a, b = 5, 10
print('{0} * {1} = {2}'.format(a,b,a*b))
#python3.6之后，更简洁的格式化方式
a,b = 5, 10
print(f'{a} * {b} = {a * b}')

#列表操作
list1 = [1,3,5,7,100]
print(list1)
#乘号表示列表元素的重复
list2=['hello'] *3
print(list2)
#计算列表长度（元素个数）
print(len(list1))
#下标(索引)运算
print(list1[0])
print(list1[4])
#print(list1[5])#IndexError: list index out of range
print(list1[-1])
print(list1[-3])
list1[2] = 300
print(list1)
#玄幻用下标便利列表元素
for index in range(len(list1)):
    print(list1[index])
#for玄幻编列列表元素
for elem in list1:
    print(elem)
#通过enumerate函数处理列表之后再便利可以同事获得元素索引和值
for index, elem in enumerate(list1):
    print('==',index, elem)

#向列表中添加元素以及从列表中移除元素
list1 = [1,3,5,7,100]
#添加元素
list1.append(200)  #[1, 3, 5, 7, 100, 200]
list1.insert(1,400) #[1, 400, 3, 5, 7, 100, 200]
#合并两个列表
#list1.extend([1000,2000]) #[1, 400, 3, 5, 7, 100, 200, 1000, 2000]
list1 += [1000,2000]
print(list1)
print(len(list1))
#先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)  #[1, 400, 5, 7, 100, 200, 1000, 2000]
#从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) #[400, 5, 7, 100, 200, 1000]
#清空列表元素
list1.clear()
print(list1)  #[]

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
#列表切片
fruits2 = fruits[1:4]  #fruits2 = fruits[1:4]
print(fruits2)
#可以通过完整切片操作来复制列表
fruits3 = fruits[:]  #['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
print(fruits3)
fruits4 = fruits[-3:-1]  #['pitaya', 'pear']
print(fruits4)
#可以通过反向切片操作来获得倒序后的列表的拷贝
fruits5 = fruits[::-1]  #['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
print(fruits5)

#列表排序操作
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
#sorted函数返回列表排序后的拷贝不会修改传入的列表
#函数的设计就应该像sorted函数一样尽可能不产生副作用 reverse 倒序
list3 = sorted(list1, reverse=True) #['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
#通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)  #['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
#给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)

#生成式和生成器
#列表的生成式语句来创建列表
f = [x for x in range(1, 10)] #[1, 2, 3, 4, 5, 6, 7, 8, 9]
f = [x + y for x in 'ABCDE' for y in '1234567']  #['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']
#用列表的生成表达式语法创建列表容器
#用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)] #[1, 4, 9, 16, 25, 36, 49, ]
#查看对象占用内存的字节数
print(sys.getsizeof(f)) #9024
print(f)
#下面的代码创建的不是一个列表而是一个生成器对象
#通过生成器可以获取到数据但不占用额外的空间存储数据
#每次需要数据的时候就通过内部的运算得到数据（需要花费额外的时间
f = ( x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))  #相比生成式生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)
#通过yield关键字将一个普通函数改造成生成器函数
#演示实现一个生成斐波那契数列的生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        yield a
def main():
    for val in fib(20):
        print(val)
if __name__ == '__main__':
    main()

#元组
t = ('李超', 29, True, '北京')
print(t)
#获取元组中的元素
print(t[0])
print(t[3])
#便利元组中的值
for member in t:
    print(member)
#重新给元组赋值
#t[0] = '王大锤'  #TypeError
#变量t重新引用了新的元组原来的元组被回收
t = ('王大锤', 20, True, '云南')
print(t)
#将元组转换成列表
person = list(t)
print(person)
#列表可以修改元素
person[0] = '李小龙'
person[1] = 25
print(person)
#将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

#集合 不允许有重复元素，可以进行交集、并集、差集运算
set1 = {1,2,3,3,3,2}
print(set1)
print('Length = ', len(set1))
#创建集合的构造器语法
set2 = set(range(1, 10))
set3 = set((1,2,3,3,2,1))
print(set2, set3)
#创建集合的推导式语法（推导式也可以用于推到集合）
set4 = {num for num in range(1,100) if num % 3 == 0 or num % 5 == 0}
print(set4)
#向集合添加元素和从集合删除元素
set1.add(4)
set1.add(5)
set2.update([11,12])
#discard删除
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1,set2)
#pop从开始删除第一个
print(set3.pop())
print(set3)
#集合的成员、交集、并集、差集等运算、对称差运算
print(set1 & set2)
#print(set1,intersection(set2))

print(set1 | set2)
#print(set1.union(set2))

print(set1 - set2)
#print(set1.difference(set2))

print(set1,set2)
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

#判断子集和超集
print(set2 <= set1)
#print(set2.issubset(set1))

print(set3 <= set1)
print(set3.issubset(set1))

print(set1 >= set2)
print(set1.issuperset(set2))

print(set1 >= set3)
print(set1.issuperset(set3))

#字典
#创建字典的字面量语法
scores = {'李超': 95, '白':78, '刘': 82}
print(scores)
#创建字典的构造器语法
items1 = dict(one=1,two=2,three=3,four=4)
#通过zip函数将两个序列 压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))
#创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1,10)}
print(items1,items2, items3)
#通过键可以获取字典中对应的值
print(scores['李超'])
print(scores['刘'])
#对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
#
scores['白'] = 65
scores['王五'] = 71
scores.update(冷面=67,放弃和=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天', 60))
#删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('李超', 100))
#清空字典
scores.clear()
print(scores)

#屏幕上显示跑马灯文字
import os
import time

def main():
    content = '北京欢迎你....'
    while True:
        #清理屏幕上的输出
        os.system('clear')    #os.system('clear')
        print(content)
        #休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()

#设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random

def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code
print(generate_code())

#函数返回给定文件名的后缀名
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
print(get_suffix("test1.py"))

#函数返回传入列表中最大和第二大的值
def max2(x):
    m1, m2 = (x[0], x[1] if x[0] > x[1] else (x[1], x[0]))
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2
x=[3,2,10,1,20,16]
print(max2(x))

#计算指定的年月日是这一年的第几天
def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    :param year: 年份
    :return: 闰年返回True 平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year,month,date):
    """
    计算传入的日志是这一年的第几天
    is_leap_year为True执行列表中右边的内容否则执行左边
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap_year(year)]
    total = 0
    for index in range(month -1):
        total += days_of_month[index]
    return total + date
def main():
    print(which_day(2022,11,20))

if __name__ == '__main__':
    main()

#打印杨辉三角形
def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col]+yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()
if __name__ == '__main__':
    main()

#双色球选号
from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    #sample()方法返回一个列表，其中包含从序列中随机选择的指定数量的项目。
    #此方法不会更改原始序列。
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()

"""
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下
来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围
成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的
人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的
，哪些位置是基督徒哪些位置是非基督徒。
"""
def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        print(index)
        index %= 30
        print('a',index)
    for person in persons:
        print('基' if person else '非', end='')
if __name__ == '__main__':
    main()

#井字棋游戏
import os

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋,请输入位置： ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('clear')
            print_board(curr_board)
        choice = input('再玩一局？(yes|no)')
        begin = choice == 'yes'
if __name__ == '__main__':
    main()