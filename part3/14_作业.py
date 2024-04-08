import random


class Game:
    top_score = 0  # 游戏的最高分数记录
    top_score_player = ""

    def __init__(self, name):  # 初始化游戏实例
        """
        初始化一个游戏实例。

        参数:
        name (str): 游戏者的名称。
        """
        self.name = name

    @staticmethod
    def show_help():  # 显示游戏帮助信息
        """
        打印游戏的帮助信息。
        """
        print("这是游戏帮助信息")

    @classmethod
    def show_top_score(cls):  # 显示当前游戏的最高分数
        """
        打印当前游戏的最高分数。
        """
        print(f"游戏的最高分为:玩家{Game.top_score_player}分数:{Game.top_score}")

    def start_game(self):  # 开始一局游戏并更新最高分数
        """
        开始一局游戏，生成一个随机得分，并根据这个得分更新最高分数。
        """
        score = random.randint(10, 100)  # 生成10到100之间的随机得分
        print(f"本次游戏得分为{score}")
        if score > Game.top_score:  # 如果当前得分高于最高分数，则更新最高分数
            Game.top_score = score
            Game.top_score_player = self.name
        else:
            pass  # 如果当前得分不高于最高分数，则不做任何操作


xw = Game("小王")
xw.start_game()
xw.show_top_score()
xh = Game("小红")
xh.start_game()
xh.show_top_score()
xl = Game("小李")
xl.start_game()
xl.show_top_score()
xz = Game("小张")
xz.start_game()
xz.show_top_score()
