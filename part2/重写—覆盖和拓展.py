# 覆盖
# class xiaoTianQiuan(Dog):
#     def bark(self):
#         print('嗷嗷叫')
# xtq=xiaoTianQiuan()
# xtq.bark()

#拓展

class Dog:
    def bark(self):
        print('汪汪叫')
        print('汪汪叫')
class xiaoTianQiuan(Dog):
    #1.先嗷嗷叫（新功能）2.汪汪叫（父类中的功能）3，嗷嗷叫（新功能）
    def bark(self):
        print('嗷嗷叫')
        # 调用父类的方法
        super().bark()
        print('嗷嗷叫')
xtq=xiaoTianQiuan()
xtq.bark()