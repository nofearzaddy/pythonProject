class person:
    def __init__(self, name, age):
        self.name = name
        # 私有的本质是python解释器执行代码，，会将这个名字重命名
        # 会在这个名字的前面加上_类名前缀，即self._age==>self._person__age
        self.__age = age  # 将其定义为私有属性，私有属性只能在类内部访问，属性名前加两个下划线__

    def __str__(self):  # 在类内部可以访问私有属性
        return '姓名：%s,年龄：%s' % (self.name, self.__age)


no_fear = person('nofear', 18)
print(no_fear)
print(no_fear.__dict__)
# # 在类外部访问age属性
# print(no_fear.__age)  # 在类外部访问私有属性，报错
# #直接修改age属性
no_fear.age = 20  # 这不是修改私有属性，是添加一个公有属性__age、
no_fear._person__age = 20
print(no_fear)
print(no_fear._person__age)  # 通过类名._类名__私有属性名,能用但是不要用，因为python解释器执行代码，会将名字重命名，
# 对象._dict_ 魔法属性可以将对象具有的属性组成字典返回
