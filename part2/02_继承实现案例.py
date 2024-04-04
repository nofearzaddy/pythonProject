class Animal:
    def eat(self):
        print('吃')


class dog(Animal):  # 定义狗类继承动物类
    def bark(self):
        print('叫,汪汪汪')


class xtq(dog):  # 定义哮天犬类继承狗类
    pass


# 创建动物类和狗类对象
a = Animal()
a.eat()
d = dog()
d.bark()
d.eat()
x = xtq()
x.bark()
x.eat()
