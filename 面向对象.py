#@property装饰器
#访问属性可以通过属性的getter(访问器)和setter(修改器)方法进行对应的操作
#使用@property包装器来包装getter和setter方法

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    #访问器 - getter 方法
    @property
    def name(self):
        return self._name

    #访问器 - getter 方法
    @property
    def age(self):
        return self._age

    #修改器 - setter 方法
    @age.setter
    def age(self, age):
        self._age = age
    @age.setter
    def name(self, name):
        self._name = name

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.name = "sssz"
    person.play()

if __name__ == '__main__':
    main()

#__slots__魔法
#需要限定自定义类型的对象只能绑定某些属性，通过在类中定义__slots__变量进行限定。
#需要注意的是__slots__的限定支队当前类的对象生效，对子类不起任何作用

class Person(object):
    #限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        return self._age

    @age.setter
    def name(self, name):
        return self._name

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋。' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def main():
    person =Person('王大锤',22)
    person.play()
    person._gender = '男'
    person.play()

if __name__ == '__main__':
    main()

#静态方法和类方法
from math import  sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and b+c >a and a+c >b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() /2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))

def main():
    a, b, c = 3,4,5
    #静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        #也可以通过给类发消息来调用对象方法但是要传入接受消息的对象作为参数
        print(Triangle.perimeter(t))
        #print(t.area())
        #print(Triangle.area(t))
    else:
        print('无法构成三角形')

if __name__ == '__main__':
    main()

# 类方法
# 第一个参数约定名为cls,通过这个参数可以获取和类相关的信息并且可以创建出类的对象
from time import time, localtime, sleep


class Clock(object):
    """
    数字时钟
    """

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

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
        return '%02d:%02d:%02d' % (
            self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()

#继承和多态

class Person(object):
    """
    人
    """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s在愉快的玩耍。' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s 在看电影.' % self._name)
        else:
            print('%s 在看熊出没.' % self._name)

class Student(Person):
    """
    学生
    """
    def __init__(self,name,age,grade):
        super().__init__(name, age)
        self._grade = grade
    #年级
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade
    #学习，课程
    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))

class Teacher(Person):
    """
    老师
    """
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s %s正在讲%s...' % (self._name, self._title, course))

def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('王三', 38, '专家')
    t.teach('python 设计')
    t.watch_av()

if __name__ == '__main__':
    main()

#子类对父类进行重写(override)
#通过方法重写可以让父类的同一个行为在子类中拥有不同的实现版本，调用经过子类重写的方法时，
#不同的子类对象回表现出不同的行为，这就是多态(poly-morphism)
from abc import ABCMeta, abstractmethod

#Pet类被处理成一个抽象类，不能够创建对象的类，通过abc模块的ABCMeta元类和abstractmethod包装器
#来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化。当main函数中调用该方法时，
#这个方法就表现除了多态行为(同样的方法做了不同的事情)
class Pet(object, metaclass=ABCMeta):
    """
    宠物
    """
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """
        发出声音
        :return:
        """
        pass

class Dog(Pet):
    """
    狗
    """
    def make_voice(self):
        print("%s: 汪汪汪。。。" % self._nickname)

class Cat(Pet):
    """
    猫
    """
    def make_voice(self):
        print('%s: 喵。。。喵。。。' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()