def add(a,b):
    return a+b

def func():
    print('我是tools模块中的func函数')
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def play(self):
        print(f'{self.name}在快乐地玩耍')

#调用函数
if __name__=='__main__':

    print('在代码中调用函数')
    print(add(1,2))
    print(add(10,20))
    print('tools:',__name__)
else:
    pass
