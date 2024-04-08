import json

def get_data():
    """
    从 'info3.json' 文件中读取数据，并将其转换为包含用户名、密码和期望值的元组列表。

    参数:
    无

    返回值:
    new_list: 包含从json文件中读取的数据的列表，每个元素是一个元组，元组中包含用户名、密码和期望值。
    """
    with open('info3.json',encoding='utf-8') as f:
        data = json.load(f)  # 加载json文件数据
        new_list=[]  # 初始化一个空列表，用于存储处理后的数据

        # 遍历json数据，将每个条目的用户名、密码和期望值提取出来，组成元组，并添加到新列表中
        for i in data:
            new_list.append((i.get('username'),i.get('password'),i.get('expect')))

        print(new_list)  # 打印处理后的数据列表
    return new_list
