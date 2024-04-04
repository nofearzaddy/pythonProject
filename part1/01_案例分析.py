class Person:
    def __init__(self, n, w):
        self.name = n
        self.weight = w

    def __str__(self):
        return f'姓名:{self.name},体重:{self.weight}kg'

    def run(self):
        print(f'{self.name}跑步5km 体重减少了{0.5}')
        # 减体重，即修改属性
        self.weight -= 0.5
    def eat(self):
        print(f'{self.name}大餐一顿 体重增加了{0.5}')
        # 增加体重，即修改属性
        self.weight += 0.5


xm = Person('小明', 75.0)
xm.eat()
xm.run()
xm.eat()
print(xm)