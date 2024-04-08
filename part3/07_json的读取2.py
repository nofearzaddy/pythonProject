import json

# 打开并读取json文件，将内容加载到列表中
with open('info2.json', encoding='utf-8') as f:
    info_list = json.load(f)

    # 遍历列表，打印每个人的信息：名字、年龄和所在城市
    for info in info_list:
        print(info.get('name'), info.get('age'), info.get('address').get('city'))

