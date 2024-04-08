class Animal:
    """
    动物类，定义了动物的基本行为。
    """
    def eat(self):
        """
        吃东西的行为。

        参数:
        self - 对象本身的引用。

        返回值:
        无
        """
        print("吃")

    def drink(self):
        """
        喝水的行为。

        参数:
        self - 对象本身的引用。

        返回值:
        无
        """
        print("喝")

    def sleep(self):
        """
        睡觉的行为。

        参数:
        self - 对象本身的引用。

        返回值:
        无
        """
        print("睡")


class Dog(Animal):
    """
    狗类，继承自动物类，定义了狗的特有行为。
    """
    def bark(self):
        """
        狗叫的行为。

        参数:
        self - 对象本身的引用。

        返回值:
        无
        """
        print("叫")


# 创建一个狗的对象
dog = Dog()
# 让狗叫
dog.bark()
# 让狗吃东西
dog.eat()
# 让狗喝水
dog.drink()

