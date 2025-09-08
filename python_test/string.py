# String
s = 'hello world'
print(s)
print(s[0:-1])
print(s[0:5])
print(s[6:])
# 字符串的长度
print(len(s))
# 字符串的查找
print(s.find('llo'))
# 字符串的替换
# replace()：替换字符串中的指定内容
print(s.replace('world','python'))
# 字符串的分割
# split()：将字符串按照指定的分隔符进行分割
# split()：默认是空格
print(s.split())
# split('l')：按照l进行分割
# split('l')：默认是空格
print(s.split('l'))
# 字符串的拼接
# +：拼接字符串
# *：重复字符串
print('hello'+'world')
print('hello'*3)
# 字符串的格式化
# %：格式化字符串
# format()：格式化字符串
# format_map()：格式化字符串
print('hello %s'%'world')
print('hello %s,age %d' % ('world',18))
print('hello {0},age {1}'.format('world',18))
print('hello {name},age {age}'.format(name='world',age=18))
print('hello {name},age {age}'.format_map({'name':'world','age':18}))
# 字符串的对齐
# center()：居中对齐
# ljust()：左对齐
# rjust()：右对齐
# zfill()：填充字符串
print('hello world'.center(20,'*'))
print('hello world'.ljust(20,'*'))
print('hello world'.rjust(20,'*'))
print('hello world'.zfill(20))
# 字符串的去空格
# strip()：去掉字符串首尾的空格
# lstrip()：去掉字符串左边的空格
# rstrip()：去掉字符串右边的空格
print(' hello world '.strip())
print(' hello world '.lstrip())
# 字符串的大小写
# upper()：将字符串转换为大写
# lower()：将字符串转换为小写
# title()：将字符串的每个单词的首字母转换为大写
print(s.upper())
print(s.lower())
print(s.title())
# 字符串的判断
# isalpha()：判断字符串是否只包含字母
# isdigit()：判断字符串是否只包含数字
# isalnum()：判断字符串是否只包含字母和数字
# isspace()：判断字符串是否只包含空格
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.isspace())
# 字符串的切片
# 字符串的切片的语法：[开始索引:结束索引:步长]
# 开始索引：默认是0
# 结束索引：默认是字符串的长度
# 步长：默认是1
print(s[::2])
print(s[::-1])
print(s[0:5:2])