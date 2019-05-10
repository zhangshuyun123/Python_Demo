# -*- coding:utf8 -

#    函数返回“东西”
#    函数中调用函数
#    20190510

#加法
def add(a, b):
    print("两个值相加 %r + %r = " %(a, b))
    return a + b

#减法
def subtract(a,b):
    print("两个值相减 %r - %r = " %(a, b))
    return a - b

#乘法
def multiplication(a, b):
    print("两个值相乘 %r * %r = " %(a, b))
    return a * b

#除法
def division(a, b):
    print("两个数相除 %r / %r " %(a, b))
    return a / b

print("Let's do some match with just functions !!")

he = add(10, 20)
sheng = subtract(200, 100)
cheng = multiplication(6, 6)
chu = division(9, 3)
print("和为：%r , 减为：%r , 乘积为：%r , 除为：%r ." %(he, sheng, cheng, chu))

print("**************************************************************")
what = add(he, subtract(sheng, multiplication(cheng, division(chu, 2))))

print("这个值变成了：", what, "你算对了吗？？")

#########################################################
# 用input()输入多个值
q, w, e, r = input("请输入值中间用空格隔开：").split()
print(q, w, e, r)