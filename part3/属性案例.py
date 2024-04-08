class Dog:
    # 定义一个表示狗的类
    count = 0  # 类属性，用于记录Dog类的实例数量

    def __init__(self, name):
        """
        初始化Dog类的实例。

        参数:
        name: 字符串，表示狗的名字。
        """
        self.name = name  # 实例属性，存储狗的名字
        Dog.count += 1  # 增加Dog类的实例数量


# 访问类属性，显示当前Dog类的实例数量
print(Dog.count)  # 输出: 0

# 创建第一个Dog实例
d1 = Dog('小黑')
print(Dog.count)  # 输出: 1

# d2仅赋值为Dog类，未创建实例，故实例数量不变
d2 = Dog
d3 = d2
print(Dog.count)  # 输出: 1

# 创建第二个Dog实例
d4 = Dog('小黄')
print(Dog.count)  # 输出: 2

# 创建第三个Dog实例
d5 = Dog('小绿')
print(Dog.count)  # 输出: 3
# 访问类属性，显示当前Dog类的实例数量
print(Dog.count)  # 输出: 3


# 可以使用实例对象.属性名来获取属性值（原因，实例对象属性的查找顺序是：先在实例对象属性中找，
# 找到直接使用，如果找不到，再在类属性中找，找到了可以使用，如果找不到，报错）
