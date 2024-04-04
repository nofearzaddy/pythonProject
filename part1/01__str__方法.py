class cat:
    # 定义添加属性的方法
    def __init__(self, name, age):
        self.name = name  # 给对象添加name属性
        self.age = age  # 给对象添加age属性

    # 输出属性信息
    # def show_info(self):
    #     print(f'小猫的名字是：{self.name},年龄是：{self.age}')

    def __str__(self):
        # 方法必须返回一个字符串，只要是字符串就行
        return f'小猫的名字是：{self.name},年龄是：{self.age}'


# 创建对象
blue_cat = cat('蓝猫', 2)
print(blue_cat)
# blue_cat.show_info()
black_cat = cat('白猫', 3)
print(black_cat)
# black_cat.show_info()
