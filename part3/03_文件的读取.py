"""
函数：读取并打印文件内容
参数：
- 文件名：'a.txt'，指定要打开并读取的文件名
- 模式：'r'，以只读模式打开文件；如果文件不存在，会抛出异常
- 编码：'utf-8'，指定文件的编码格式
返回值：无
"""

# 打开文件
f = open('a.txt', 'r', encoding='utf-8')

# 读取文件内容并打印
buf = f.read()
print(buf)

# 关闭文件
f.close()

# 注意：该代码以只读模式打开文件，如果文件不存在，会抛出异常

