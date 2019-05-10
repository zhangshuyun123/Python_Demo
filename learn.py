# 字符串
X = "这里有 %d 个人" %10
print(X)

name = "张淑赟"
intereset = "Play basketball"
intrudoce = "My name is %s ,I like %s" %(name,intereset)
print(intrudoce)
print("我说：%s" %X)
print("做自我介绍：%r" %intrudoce)

day = "Thursday"
print("Today is ",day)
print('''
	这是↑
	我↑
	学习↑
	Python↑
	的第一天↑
	''')

#格式化输出十六进制
nHex = 0x20
print("十六进制是","nHex = %x" %nHex)
#格式化输出十进制
print("十进制是","nDec = %d" %nHex)
#格式化输出八进制
print("八进制是","nOct = %o" %nHex)

#格式化输出浮点数
import math
print("π = %f" %math.pi)
print("π = %r" %math.pi)

# %r 是万能格式输出

print("π = %10.3f" %math.pi) #打印输出前有10个字符，保留3位小数点
print("π = %10.3r" %math.pi)
print("π = %06d" %int(math.pi)) # int(math.pi)类型转换，%06d共输出6个数前面不够用0补充

###############################################################################################

#列表
list = [1,2,3,4,'hello',"张淑赟",99.999]
print(list)
'''字典'''
dict = {1:'A',2:'B',3:"C",4:99.9}
print(dict)

##############################################################################################

#简单的交互input
print("你叫什么名字？？")
my_name = input()
print("你叫 %r 对吗？？" %my_name)
age = input("How old are you ? ")
print("所以你叫 %r ,今年 %r 岁了吗？" %(my_name,age))

##############################################################################################
