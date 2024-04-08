import json

# 定义一个列表，包含用户登录信息
my_list = [('admin', '123456', '登录成功'), ('root', '123456', '登录失败'), ('admin', '123123', '登录失败')]

# 打开一个文件，准备将列表信息写入到JSON文件中
with open('info4.json', 'w', encoding='utf-8') as f:
    # 将Python对象（列表）转换为JSON格式，并写入到文件中
    # 同时设置ensure_ascii=False以确保中文能够正常输出，indent=2使得输出的JSON格式化，易于阅读
    json.dump(my_list, f, ensure_ascii=False, indent=2)

