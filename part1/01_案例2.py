# class House:
#     def __init__(self, n, t):
#         self.name = n
#         self.total_area = t
#         self.free_area = t
#         self.item_list = []
#
#     def add_item(self, item):
#         self.item_list.append(item.name)
#         self.free_area -= item.area
#
#     def __str__(self):
#         return f'房子{self.name}占地{self.total_area},剩余面积{self.free_area},家具有{self.item_list}'
#
#
# class HouseItem:
#     def __init__(self,name,area):
#         self.name =name
#         self.area =area
#
#     def __str__(self):
#         return f'{self.name}占地{self.area}'
#
#
# bde = HouseItem('席梦思', 40)
# chest = HouseItem('衣柜', 20)
# table = HouseItem('餐桌', 30)
# print(bde)
# print(chest)
# print(table)
# z = House('珠江帝景', 2000)
# z.add_item(bde)
# print(z)


# 定义家具类
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'{self.name}占地{self.area}'


class House:
    def __init__(self, name, area):
        self.name = name
        self.total_area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return f'房子{self.name}占地{self.total_area},剩余面积{self.free_area},家具有{self.item_list}'

    def add_item(self, item):  # item是一个家具对象
        # 判断剩余面积是否足够
        # self表示的房子对象，缺少一个家具对象使用传参解决
       if self.free_area >= item.area:
           self.item_list.append(item.name)
           self.free_area -= item.area
           print(f'{item.name}添加成功')
       else:
           print(f'{item.name}添加失败')


# 创建家具对象
bed = HouseItem('席梦思', 40)
chest = HouseItem('衣柜', 20)
table = HouseItem('餐桌', 30)
print(bed)
print(chest)
print(table)
z = House('珠江帝景', 2000)
# 添加家具
z.add_item(bed)
# 打印房子
print(z)