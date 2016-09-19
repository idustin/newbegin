#! /usr/bin/python
# -*- coding:utf-8 -*-

print('hey new python new begin!!!')

# a = raw_input('please enter a: ')

a = 100
if a >= 0:
	print(a)

else:
	print(-a)




# 计算机由于使用二进制，所以，有时候用十六进制表示整数比较方便，十六进制用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。

# 浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。

# 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的，除法也是精确的，而浮点数运算则可能会有四舍五入的误差。

# 在Python中，可以直接用True、False表示布尔值（请注意大小写）  布尔值可以用and、or和not运算。

# not运算是非运算，它是一个单目运算符，把True变成False，False变成True

# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

# 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量  请不要把赋值语句的等号等同于数学的等号

# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言

# 因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。

# 最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255）

# 如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是65535，4个字节可以表示的最大整数是4294967295。

# 由于计算机是美国人发明的，因此，最早只有127个字母被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。

# 但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。

# 全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。

# 因此，Unicode（1990年开始研发，1994年正式公布。）应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。

# Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。

# ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。

'''
字母A用ASCII编码是十进制的65，二进制的01000001；

字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；

汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。
'''

# 如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。

# 新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

# 所以，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。

# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。

# 如果要传输的文本包含大量英文字符，用UTF-8编码就能节省空间

# 浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器

# %x : 十六进制整数



# list: Python内置的一种数据类型是列表 list是一种有序的集合，可以随时添加和删除其中的元素。

classmates = ['python','c','object-c','ios']

print(classmates)

print(len(classmates))


# list是一个可变的有序表，所以，可以往list中追加元素到末尾：

classmates.append('java')

print(classmates)


# 也可以把元素插入到指定的位置，比如索引号为1的位置：

classmates.insert(1, 'html')

print(classmates)


# 要删除list末尾的元素，用pop()方法：

classmates.pop()
print(classmates) 

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：

classmates.pop(1)

print(classmates)


# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：

classmates[0] = 'py'

print(classmates)

# list里面的元素的数据类型也可以不同  list元素也可以是另一个list

s = ['python','java',['html','javascript'],'scheme']         
print(len(s)) # 4




# tuple和list非常类似，但是tuple一旦初始化就不能修改

# 它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

# 当定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

# 可以定义一个空的tuple

t = ()

print(t)


# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：

t = (1,)
print(t)




# 循环

# 第一种loop是 for x in ......
language = ['python','java','cs','object-c','iso']

for i in language:
	print(i)
	



sum = 0

nums = [1,2,3,4,5,6,7,8,9,10]

for x in nums:
	sum += x
	
print(sum)



print(list(range(101)))



sum = 0

for i in range(101):
	sum += i
	
print(sum)




# 第二种loop是while

# while只要条件满足，就不断循环，条件不满足时退出循环。比如要计算100以内所有奇数之和，可以用while循环实现

sum = 0

n = 99

while n > 0:
	sum += n
	n -= 2
	
print(sum)
# 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。





# dictionary:
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

d = {'zhang':0,'fu':100,'lulu':100,'su':100}

print(d['zhang'])

print(d['fu'])

print(d['lulu'])

print(d['su'])




# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

# 如果key不存在，dict就会报错

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

print('zhang' in d)  # >>> Ture

print('xiao' in d)   # >>> False


# 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：

print(d.get('feng')) # >>> None  注意 d.get() 不是 d.get[]

print(d.get('zhangzhang'),-1) # >>> -1

# 注意：返回None的时候Python的交互式命令行不显示结果。



# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：

d.pop('zhang')

print(d)  # >>> {'lulu': 100, 'fu': 100, 'su': 100}


# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。


# dict和list比较，dict有以下几个特点:
'''

1、查找和插入的速度极快，不会随着key的增加而变慢；

2、需要占用大量的内存，内存浪费多。


而list相反：

1、查找和插入的时间随着元素的增加而增加；

2、占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。

'''
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key



# set:
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# 要创建一个set，需要提供一个list作为输入集合：
# set : set()

s = set([111,222,333])

print(s)  # >>> {333, 222, 111}

# 注意，传入的参数[111,222,333]是一个list，而显示的{111, 222, 333}只是告诉这个set内部有111，222，333这3个元素，显示的顺序也不表示set是有序的。

# 重复元素在set中自动被过滤

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果

s.add(444) 

print(s)  # >>> {444, 333, 222, 111}

# 通过remove(key)方法可以删除元素：

s.remove(444)

print(s) # >>> {333, 222, 111}


# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

s1 = set([1,2,3])

s2 = set([2,3,4,5,6])

print(s1 & s2) # >>> {2,3}

print(s1 | s2) # >>> {1,2,3,4,5,6}

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。



# str是不变对象，而list是可变对象
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

a = ['99','11','88','33','66','22']

a.sort()

print(a) # >>> ['11', '22', '33', '66', '88', '99']


# 而对于不可变对象，比如str，对str进行操作呢：

b = 'abcdefg'

b.replace('a','AA')

print(b) # >>> 仍然是abcdefg


b = 'abcdefg'

c = b.replace('a', 'A')

print(c) # >>> Abcdefg

# 这是因为 ：要始终牢记的是，a是变量，而'abcdefg'才是字符串对象！有些时候，经常说，对象a的内容是'abcdefg'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abcdefg'



# 函数：
# 圆的面积计算公式为 : S = πr2


































































