#定义类
class Student(object):
    #__init__ 是一个特殊方法用于在创建对象时进行初始化操作
    #通过这个方法可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s 正在学习 %s.' % (self.name, course_name))

    #PER 8要求标识符的名字用全小写多个单词用下划线链接
    def watch_movie(self):
        if self.age < 18:
            print('%s 只能观看《熊出没》。' % self.name)
        else:
            print('%s 观看电影。' % self.name)

#创建和使用对象
def main():
    #创建学生对象并指定姓名和年龄
    stu1 = Student('刘', 38)
    #给对象发study消息
    stu1.study('Python程序设计')
    #给对象发watch_av消息
    stu1.watch_movie()
    stu2 = Student('王',15)
    stu2.study('思想品德')
    stu2.watch_movie()

if __name__ == '__main__':
    main()

#访问可见性
#属性和方法的的访问权限有两种，公开/私有，私有属性用两个下划线开头

class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')

def main():
    test = Test('hello')
    test.__bar()
    print(test.__foo)

if __name__ == '__main__':
    main()

# 描述数字时钟
from time import sleep


class Clock(object):
    """
    数字时钟
    """

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """
        走字
        :return:
        """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """
        显示时间
        :return:
        """
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()

#定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

from math import sqrt

class Point(object):

    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return:
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        移动指定的增量
        :param dx: 横坐标的增量
        :param dy: 纵坐标的增量
        :return:
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算与另一个点的距离
        :param other: 另一个点
        :return:
        """
        dx = self.x - other.x
        dy = self.y - other.y

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print('p2', p2)
    p2.move_by(-1,2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()

