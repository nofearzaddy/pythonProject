# 此段代码用于演示Python中try-except-else-finally块的基本用法
# 尝试从用户输入获取一个数字，并进行一系列操作
try:
    # 尝试将用户输入转换为整数
    num = input('请输入数字:')
    num = int(num)
    print(num)
    # 尝试进行除法运算
    a = 10 / num
    print(f'a:{a}')
except Exception as e:
    # 如果发生任何异常，打印异常信息
    print(f"错误信息:{e}")
else:
    # 如果没有发生异常，执行此块
    print('没有异常,我会执行')
finally:
    # 不管是否发生异常，都会执行此块
    print('不管有没有异常,我都会执行')

