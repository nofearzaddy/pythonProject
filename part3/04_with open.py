"""
向文件'a.txt'追加内容。

函数不接受参数，也不返回任何值。

步骤：
1. 以追加模式打开文件'a.txt'，确保现有内容不会被覆盖，同时指定编码为utf-8。
2. 向文件中写入'good good study\n'，该行文本将会在文件末尾添加。
"""
with open('a.txt', 'a', encoding='utf-8') as f:
    f.write('good good study\n')

# a方式打开文件，文件不存在会创建文，文件存在在文件末尾写入内容
