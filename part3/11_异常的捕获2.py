# 尝试从用户输入获取一个数字，并进行一系列操作
try:
    num=input('请输入数字:')  # 提示用户输入数字
    num=int(num)  # 尝试将用户输入转换为整数
    print(num)  # 打印输入的数字
    a=10/num  # 尝试进行除法运算
    print(f'a:{a}')  # 打印除法运算结果
except ValueError:
    print('发生了异常，请输入正确的数字...')  # 当用户输入无法转换为整数时，捕获ValueError异常
except ZeroDivisionError:
    print('除数不能为0')  # 当除数为0时，捕获ZeroDivisionError异常
