# my_dict2 = {"name": "无畏", "age": "18", "height": "183", "is_men": True, "like": ["打野", "辅助", "双冠野王"]}
# for key in my_dict2.keys():
#     print(key)
# for value in my_dict2.values():
#     print(value)
class Nofear:
    def __init__(self, name, age, like, height):
        self.name = name
        self.age = age
        self.like = like
        self.height = height

    def prin(self):
        # print('姓名':self.name‘,'年龄':self.age，'爱好':self.like,'身高':self.height)
        print(f"姓名: {self.name}, name:{self.age}, 年龄:{self.age}, 爱好:{self.like}, 身高:{self.height}")


nofear = Nofear('无畏', '18', '打野，辅助，双冠野王', '183')
nofear.prin()
