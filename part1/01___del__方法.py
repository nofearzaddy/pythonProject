class Demo:
    def __init__(self, n):
        print('我是__init__,我被调用了')
        self.name = n

    def __del__(self):
        print(f'{self.name}没了,终于倒闭了')


# Demo('hero')
a = Demo('hero1')
b = Demo('hero2')
del a  # 删除
print('代码运行结束')
