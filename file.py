#对文件的操作
#将新加入的内容覆盖了原有内容

'''
#读取文件中的内容

from sys import argv
script,filename = argv
txt = open(filename)
print("这是你要打开的文件：%r" %filename)
print(txt.read())
print("再次打开文件")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())

'''

#打开文件
from sys import argv
script,filename_1 = argv
print("这个脚本名字叫 %r" %script)
print("要打开的文件为：%r" %filename_1)
target = open(filename_1,'w')
target.truncate()

print("现在开始添加")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")
line4 = input("line4:")
'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write(line4)
target.write("\n")
'''
target.write(" %r\n %r\n %r\n %r\n" %(line1,line2,line3,line4))
print("写入结束，关闭文件")
target.close()
txt_1 = open(filename_1)
print(txt_1.read())