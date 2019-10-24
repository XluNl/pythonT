print('re_model')

import re
#print(help(re))
s = 'hello world'
a = s.find('d') #返回的是字符 出现的位置
a = s.replace('ll','bb')
a = s.split(' ')
#print(a)

r = re.findall('clp','3412clp4241241234clp344clp453')
print(r)

#元字符
#.:只能代表一个字符,代表出\n 外的任意字符
#^:只会从开始位置匹配
#$:只会结尾位置匹配
#*:重复匹配(0-0++)
#+:重复匹配(1-0++)最少有一个
#{}:匹配几次-{1,3}
#?:匹配{0,1}
#[a-z A-Z]:匹配字符集
#[^t]:除了t之外的字符
#[^4,5]:除了4和5之外的字符
#|:或者的意思
#\:1,反斜杠后面跟元字符去除特殊功能 2,反斜杠后面跟普通字符实现特殊功能
	#\d=[0-9]
	#\D = [^0-9]
	#\s = [\t\n\r\f\v]
	#\S = [^\t\n\r\f\v]
	#\w = [a-zA-Z0-9]
	#\W = [^a-zA-Z0-9]
	#\b 捕捉特殊字符,空格/$/
#(?p<id>\d{3})(?p<name>\w{3}) 组()

#.:只能代表一个字符,代表出\n 外的任意字符
r = re.findall('c.p','3412clp4241241234clp344clp453')
print(r)
#^:只会从开始位置匹配
r = re.findall('^x.p','xlp3412clp4241241234clp344clp453')
print(r)
#$:只会结尾位置匹配
r = re.findall('x.p$','clp3412clp4241241234clp344clp453xlp')
print(r)
#*:重复匹配(.任意字符.*重复匹配任意字符)
r = re.findall('s.*p$','clp3412clp4241241234clp344clp453sddlp')
print(r)
#多个a 1个b
r = re.findall('a+b','123aabfdsgabb') #['aab', 'ab']
print(r)
#多个a 多个b
r = re.findall('a+b+','123aabfdsgabb') #['aab', 'abb']
print(r)

#多个a匹配5此一个b
r = re.findall('a{5}b+','123aabfdsgaaaaaaabb') #['aaaaabb']
print(r)

#多个a匹配2此或3次多个b
r = re.findall('a{2,3}b+','123aabfdsgaaaaaaabb') #['aab', 'aaabb']
print(r)

#没有a 或1个a b结尾
r = re.findall('a?b+','123aabfdsbgaaaaaaabb') #['ab', 'b', 'abb']
print(r)

#[] a和b直接的字符要么c,要么f
r = re.findall('a[c,f]b','123aafbfdsbgaaaaacaabb') #['afb']
print(r)
r = re.findall('a[a-z]b','123aafbfdsbgaaaaacaabb') #['afb', 'aab']
print(r)
# r = re.findall('a[,]b','123aafbfdsa*bgaaaa,acaa,bb') #['afb', 'aab']
# print(

# ^放在[]里是取反的意思
r = re.findall('[^5]','12345') #['1', '2', '3', '4']
print(r)
r = re.findall('[^5,4]','12345') #['1', '2', '3']
print(r)

#\d = [0-9]
r = re.findall('\d{5}','1234545645664') #['12345', '45645']
print(r)
#\d = [0-9]
r = re.findall('\d{5}','1234545645664') #['12345', '45645']
print(r)

#\b 捕捉特殊字符边界这个例子捕捉到的是[i  ][i$]
r = re.findall(r'i\b','123454ii5645664i rrri$lldfdfsdiiig') #['['i', 'i']
print(r)

#search 找到一个就直接返回,不在查找
r = re.search('ab','1ab454564abc64').group() #[ab]
print(r)

# 匹配特殊字符 斜杠"\"
#r = re.findall('\\\\',r"1232\345346dfg\dg") #
r = re.findall(r'\\',r"\1232\345346dfg\dg\\") #加r 代表告诉python 就是没有特殊意义的字符串
print(r)

#| 或者(多个条件)
r = re.search('(ab)|3','13ab4354564abc64').group() #[3]
print(r)

r = re.findall('(ab)|3','13ab4354564abc64') #[3]
print(r)

# (?p<id>\d{3})(?p<name>\w{3}) 组
#r = re.search('(?p<id>\d{3})(?p<name>\w{3})','13ab4354564abc64').group() #[3]
#print(r)

#match
r = re.match('ab','ab4354564abc64') #[3]
print(r.group())

#split 
r = re.split('ab','ab4354564abc64') #[3]
print(r)
# 意思先使用b分,然后在使用4 对每段在进行分
r = re.split('[b,4]','ab4354564abc64') #[3]
print(r) #['a', '', '35', '56', 'a', 'c6', '']

#sub 字符串替换
r = re.sub('a..3','s..b','ab4354564abc64') #[3]
print(r) #s..b54564abc64

#compile 定义一个规则重复使用
obj = re.compile('./com')
re = obj.findall('345352523./comtddgfgdf')
print(re)
#总结
#findall 获取所有的匹配结果
#search  可调用group方法 获取每组内容
#match   只在开始位置匹配和^类似,值获取一个内容
#split   和字符串的分割一样,这里可以使用正则表达式分割
#sub     字符串替换
#compile 定义一个规则重复使用