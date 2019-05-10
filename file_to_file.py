from sys import argv
from os.path import exists

'''
script,from_file,to_file = argv

print("该脚本名称为：%r" %script)

print("目标文件是否存在？？%r" %exists(to_file))
print("源文件为：%r ,要将内容拷贝到：%r" %(from_file,to_file))

openfile = open(from_file)
indata = openfile.read()
input()
outputfile = open(to_file,'w')
outputfile.write(indata)

'''
#以上可以简化为：

script,from_file,to_file = argv
open(to_file,'w').write(open(from_file).read())


print("所有内容已拷贝完成")