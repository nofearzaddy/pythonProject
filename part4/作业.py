# f = open('test.txt', 'w', encoding='utf-8')
# f.write('wow,so beautiful!')
# f.close()
# f = open('test.txt', 'r', encoding='utf-8')
# data = f.read()
# print(data)

# with open('a.txt','w',encoding='utf-8')as f:
#     f.write('张三，李四，王五，赵六')
# with open('a.txt','r',encoding='utf-8')as f:
#     buf=f.read()
#     my_list=buf.split(',')
# print(my_list)
#
# #这个是我自己写的，上面那个是老师写的
# f = open('a.txt', 'w', encoding='utf-8')
# f.write('张三，李四，王五，赵六')
# f.close()
# f = open('a.txt','r',encoding='utf-8')
# buf=f.read()
# my_list=[]
# my_list.append(buf)
# print(my_list)

# import  json
# with open('info.json',encoding='utf-8')as f :
#     info=json.load(f)
#     print(info.get('name'))
#     print(info['like'])
#
# import  random
# with open('data.txt','w',encoding='utf-8')as f:
#     for i in range(10):
#         num=random.randint(1,20)
#         f.write(f'{num},')
# with open ('data.txt','r',encoding='utf-8')as f:
#     data=f.read()
#     data=data[:-1]
#     data_list=data.split(',')
# new_list=[]
# for i in data_list:
#     new_list.append(int(i))
# new_list.sort(reverse=True)#降序
# print(new_list)
# print(new_list[:5])

import random
import json
my_list = []
for i in range(10):
    num = random.randint(1, 20)
    my_list.append(num)
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write(str(my_list))
    json.dump(my_list, f)
with open('data.txt', 'r', encoding='utf-8') as f:
    data_list = json.load(f)
    data_list.sort(reverse=True)
    print(data_list)
    print(data_list[:5])
