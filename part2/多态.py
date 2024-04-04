# 能不能帮我改成打印出来是
# 姓名开发人员__工作是写代码
# 把我的代码复制下来在那个基础上改
# 不要破坏我源代码


class Person:
    def work(self):
        print('努力工作')


class Coder:
    # def __init__(self, name):
    #     self.name = name
    def work(self):
        print(f'开发人员__工作是写代码')


class Tester:
    def work(self):
        print(f'测试人员__工作是写测试')


class Company:
    def show_work(self, worker):
        worker.work()


c = Company()
xw = Coder()
xh = Tester()
c.show_work(xw)
c.show_work(xh)
