from sys import argv
#传参
script, input_file = argv
#读取文件中内容
def print_all(f):
    print(f.read())

#函数seek()用于移动文件读取指针到指定位置
def rewind(f):
    f.seek(1)
#打印行号并且一行一行读取
def print_a_line(line_count,f):
    print(line_count,f.readline())
#打开文件
current_file = open(input_file)

print("打印文件名称：\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.\n")

rewind(current_file)
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
