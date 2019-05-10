
from sys import argv
script,user_name = argv
prompt = '> '
print("%r 你好，我是第 %r 个脚本" %(user_name,script))
print("你的爱好是什么？？")
likes = input(prompt)
print("我和小明说你喜欢 %r" %likes)