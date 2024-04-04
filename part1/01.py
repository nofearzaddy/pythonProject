# print("hello world")
import random

while True:
    # 注释符号后面要有空格
    # 敲得多了就快了
    # 当你写代码出现一堆倾斜的东西，那就是ai给你的提示，你可以选择tab接受，或者esq拒绝
    player = int(input('请出石头(1)剪刀(2)布(3)退出（0）:'))
    if player == 0:
        break
    computer = random.randint(1, 3)
    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print('恭喜你获得胜利')
    elif player == computer:
        print('平局')
    else:
        print('输了，不要放弃再来一局')
