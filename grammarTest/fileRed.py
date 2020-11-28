# filename1 = '‪C:/Users/33054/Desktop/aa.txt'
f = open("c:/Users/33054/Desktop/aa.txt", 'r')  # mode默认是 r,这里可以不用写
# 如果txt中有中文,会遇到编码问题,应该用如下语句
# f = open('test3.txt', encoding='utf8')    #  mode='r'可以不用写
print("-------" + f.readline())

print('======' + f.read())  # 打印出读取的内容
# 这里会把txt文件中所有内容读取出来,如果txt文件过大,可能造成卡死

# 循环读取
for line in f:
    print('-----' + line)  # 循环读取文件,每次读取一行

a = f.readlines()  # 把整个文件打印出来,按照每行来区分,返回一个大的列表,列表中每个元素代表一行
print(a, type(a))  # ['line 1\n', 'line 2\n', 'line 3'] <class 'list'>
# 注意,上述 f.read()操作会把文件指针指向文件末尾,导致上句语句输出为空字符串,所以在测试时需要注释掉 f.read()


b = f.readline()  # 每次读取一行
print(b)  # line 1  (换行)<class 'str'>
b = f.readline()
print(b, type(b))  # line 2  (换行)<class 'str'>
b = f.readline()
print(b, type(b))  # line 3  (换行)<class 'str'>
# f.readline()读取txt文件中的一行文本,返回字符串.文件指针移动到当前读取行的末尾
# 同样在测试时需要注释掉 f.read()

# 如果想把文件指针移动到整个文件的开始,有两种办法:
# 1.可以先f.close()文件,再重新打开
# 2.可以通过f.seek(0)让指针回到整个文件的开始

f.close()
