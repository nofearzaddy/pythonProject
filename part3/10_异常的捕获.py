# try:
#     num=input('请输入数字:')
#     num=int(num)
#     print(num)
# except:
#     print('输入有误')
# print('h后续其它代码，可以继续执行')、
# 尝试从用户输入获取一个数字并进行运算
try:
    num=input('请输入数字:')  # 提示用户输入数字
    num=int(num)  # 尝试将输入的字符串转换为整数
    print(num)  # 打印输入的数字
    a=10/num  # 尝试进行除法运算
    print(f'a:{a}')  # 打印运算结果
except ValueError:
    print('发生了异常，请输入正确的数字...')  # 如果转换为整数失败，则捕获ValueError异常并给出提示

