"""
构造程序逻辑
寻找水仙花数(超完全数字不变数 自恋数 自幂数 阿姆斯特朗数，是一个三位数，每个位上的数字的立方之和正好等于它本身)
$ 1^3 + 5^3 + 3^3 = 153 $
"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

"""
实现讲一个正整数反转，12345  54321
"""
num = int(input("num = "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    #整除
    num //= 10
print(reversed_num)

'''
百钱百鸡
公鸡 5块1只 母鸡3块一只 小鸡1块3只 100块买100只 三种各买几只
'''
for x in range(0,20):
    for y in range(0,33):
        z = 100 - x -y
        if x * 5 + y * 3 + z / 3 == 100:
            print("公鸡 %d,母鸡 %d,小鸡 %d" % (x,y,z))

"""
CRAPS赌博游戏
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，
玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，
玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
"""
from random import randint

money = 1000
while money > 0:
    print('总资产为：',money)
    need_go_on = False
    while True:
        debt = int(input('下注：'))
        if 0 < debt <= money:
            break
    first = randint(1,6) + randint(1,6)
    print('玩家点数： %d' % first)
    if first == 7 or first == 11:
        print('玩家胜')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜')
        money -= debt
    else:
        need_go_on = True
        print('继续')
    while need_go_on:
        need_go_on = False
        current = randint(1,6) + randint(1,6)
        print('玩家点数： %d' % current)
        if current == 7:
            print('庄家胜')
            money -= debt
        elif current == first:
            print('玩家胜')
            money += debt
        else:
            need_go_on = True
print('破产了')

"""
斐波那契数列
前两个数都是1，第三个数开始，每个数都是前面两个数的和
1，1，2，3，5，8，13，21
"""
a=1
b=1
c=[a,b]
for i in range(18):
   a,b=b,a+b
   c.append(b)
print

"""
10000以内的完美数
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数
"""
for j in range(1,20):
    s = j
    for i in range(1,j):
        if j % i == 0:
            #用s减去j的因子i，等到i完成所有的遍历，相当于s减去了j的所有因子
            s -= i
    #如果s等于0，说明s减去j的所有因子值为0，也就是j等于它的所有因子之和
    if s == 0:
         print(j)

"""
100以内的素数
只能被1和自身整除的正整数(不包括1)
"""
l = []
for x in range(100):
    #判断如果ｘ是素数，则打印，如果不是素数就跳过
    if x < 2:
        continue

    for i in range(2,x):
        if x % i == 0:
            break
    else:
        l.append(x)
print(l)

