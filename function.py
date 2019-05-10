def print_any(*args):
	arg1,arg2,arg3 = args
	print("arg1: %r ,arg2: %r,arg3: %r" %(arg1,arg2,arg3))
print("1,2,3") 

def print_two(arg1,arg2): #形参
	print("两个形参是：arg1= %r ,arg2= %r" %(arg1,arg2))
print("5,10")   #实参

'''
	在定义函数（int add (int a,int b)中a和b是形参）
	在调用函数时：add(1,2)中1和2就是实参
'''
