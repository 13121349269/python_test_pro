"""
使用比那两包村数据并进行运算
"""

a = 321
b =12
print(a+b)
print(a-b)
print(a*b)
print(a/b)

"""
使用type()检车变量类型
"""
a = 100
b = 12.345
c = 1 +5j
d = "hello,world"
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

"""
int()   将一个数值火字符串转换成整数，可以指定进制
float() 将一个字符串转换成浮点数
str()   将指定的对象转换成字符串形式，可以指定编码
chr()   将整数转换成该编码对应的字符串(一个字符)
ord()   将字符串(一个字符)转换成对应的编码(整数)
"""

"""
通过输入两个整数实现算数运算
"""

a = int(input('a= '))
b = int(input('b='))

print('%d + %d = %d' % (a,b,a+b))
print('%d - %d = %d' % (a,b,a-b))
print('%d * %d = %d' % (a,b,a*b))
print('%d / %d = %d' % (a,b,a/b))
print('%d // %d = %d' % (a,b,a//b))
print('%d %% %d = %d' % (a,b,a%b))
print('%d ** %d = %d' % (a,b,a**b))

"""
运算符，优先级从高到低
[] [:]                      下标，切片
**                          指数
~ + -                       按位取反，正负号
* / % //                    乘 除 模 整除
+ -                         加 减
>> <<                       右移 左移
&                           按位与
^ |                         按位异或  按位或
<= < > >=                   小于等于 小于 大于 大于等于
== !=                       等于  不等于
is is not                   身份运算符
in not in                   成员运算符
not or and                  逻辑运算符
= += -= *= /= %= **= &= `   = ^= >>= <<=`
"""

"""
运算符和逻辑运算符
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False)

"""
华氏温度转换摄氏温度
"""
f = float(input("输入温度： "))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
#另一种格式化
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

"""
输入圆的半径计算周长和面积
"""
radius = float(input("输入圆的半径： "))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长： %.2f' % perimeter)
print('面积： %.2f' % area)

"""
输入年份判断是不是闰年
"""
year = int(input("输入年份： "))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)

"""
if 语句
"""
username = input('输入用户名：')
password = input('输入口令：')
if username == 'admin' and password == '123456':
    print('验证成功')
else:
    print('验证失败')

"""
分段函数求值
"""
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
        y = 5 * x + 3
print('f(%.2f) = %.2f' % (x,y))

"""
英制单位英寸和公制单位厘米互换
"""
value = float(input("输入长度: "))
unit = input('输入单位： ')
if unit == 'in' or unit == '英寸':
    print('%f 英寸 = %f 厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f 厘米 = %f 英寸' % (value,value / 2.54))
else:
    print('请输入有效单位')

"""
百分制成绩转换为等级制成绩
"""
score = float(input('输入成绩：'))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print('对应的等级是：', grade)

"""
输入三条边长，如果能构成三角形就计算周长和面积
"""
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a + b > c and a + c > b and b + c > a:
    print('周长是：%f ' % (a+b+c))
    p = (a+b+c) /2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积： %f' % (area))
else:
    print('不能构成三角形')