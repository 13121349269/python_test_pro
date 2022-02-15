#工资结算系统
"""
某公司有三种类型的员工，分别为部门经理、程序员和销售员
需要设计一个工资结算系统，根据员工信息来计算月薪
部门经理每月固定15000；
程序员每小时150；
销售员月薪1200加5%的提成；
"""
#@abstractmethod：抽象方法，含abstractmethod方法的类不能实例化，继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，未被装饰的可以不重写
from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    """
    员工
    """

    def __init__(self, name):
        """
        初始化方法
        :param name: 姓名
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        获得月薪
        :return: 月薪
        """
        pass

class Manager(Employee):
    """
    部门经理
    """

    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """
    程序员
    """
    def __init__(self, name, working_hour = 0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour >0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour

class Salesman(Employee):
    """
    销售员
    """
    def __init__(self, name, sales = 0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales >0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05

def main():
    emps = [
        Manager('刘'), Programmer('诸'),
        Manager('曹'), Salesman('芶'),
        Salesman('吕'), Programmer('张'),
        Programmer('赵')
    ]
    #isinstance() 函数来判断一个对象是否是一个已知的类型
    #如果要判断两个类型是否相同推荐使用 isinstance()
    for emp in emps:
        #判断emp 属于Programmer类型
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('输入%s本月工作时间： ' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('输入%s本月销售额: ' % emp.name))
        #同样是接受get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为:  ￥%s元' % (emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()