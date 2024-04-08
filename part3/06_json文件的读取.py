# 此脚本用于读取并解析一个 JSON 文件
# 1，导入 json 模块，用于处理 JSON 数据
import json
# 2，打开 JSON 文件
with open('info.json', encoding='utf-8') as f:
    # 3，使用 json.load 方法将文件内容加载为 Python 对象
    result = json.load(f)
    # 打印结果的类型，确认数据被正确解析
    print (type(result))
    # 打印 JSON 对象中 'name' 键对应的值
    print (result.get('name'))
    # 打印 JSON 对象中 'age' 键对应的值
    print (result.get('age'))
    # 打印 JSON 对象中 'address' 字典中 'city' 键对应的值
    print(result.get('address').get('city'))

