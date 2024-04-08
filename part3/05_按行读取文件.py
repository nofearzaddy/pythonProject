# 第一个代码块：逐行读取文件并打印
# 打开文件 'b.txt'，以utf-8编码读取内容
with open('b.txt', encoding='utf-8') as f:
    buf = f.readline()  # 读取文件的第一行
    print(buf)
    print(f.readline())  # 读取并打印文件的第二行

# 第二个代码块：通过for循环逐行读取并打印文件内容
# 打开文件 'b.txt'，以utf-8编码读取内容
with open('b.txt', encoding='utf-8') as f:
    for i in f:  # 遍历文件的每一行
        print(i,end='')  # 打印当前行，不换行

# 第三个代码块：通过while循环逐行读取并打印文件内容
# 打开文件 'b.txt'，以utf-8编码读取内容
with open('b.txt', encoding='utf-8') as f:
    while True:  # 持续读取文件内容
        buf = f.readline()  # 读取文件的一行
        if len(buf) == 0:  # 如果读取的行为空，则退出循环
            break
        print(buf, end='')  # 打印当前行，不换行

