#coding:utf8
#在py2 里面需要加入以下编码声明  否则输出乱码,主要是给py2.7的解释器看
import sys
print(sys.getdefaultencoding()) #py2默认ascii编码,不支持中文,所以要在文件头声明编码;py3默认utf8编码

# #  在3里面不会出错,黑窗口也不会出错,但是在2里面就会出错
# print('编码拾遗')
#
# # 这个在2里面 会打印出字节(bytes)
# print(['横说竖说'])

#/////////////////py2//////////////////
# s = '鹏鹏'#这个在py2 里面存的是bytes
# print(len(s))#6
# print(repr(s))#'\xe9\xb9\x8f\xe9\xb9\x8f',存的是字节
# print(type(s))#str
# print(s.decode('utf-8'))#把字节转换为utf8(万国码)

# s = u'哈哈哈'#字符串前面几个'u',表示unicode
# print(len(s))#6
# print(repr(s))#u'\u54c8\u54c8\u54c8',存的是uncode
# print(type(s))#<type 'unicode'>
# print(s.encode('utf-8'))#将unicode 编码为utf8

#unicode:去世界通用,所有字符都有对应

#s = 'www'+ u'ttt'#字符串前面几个'u',表示unicode,如果都是ascll码字符 则没有问题
#print('哈哈')
# s = u'嘿嘿嘿'+ u'哈哈哈'#unicode 拼接
# s = b'嘿嘿嘿'+ b'哈哈哈'#bytes 拼接
# print(len(s))#6
# print(repr(s))#u'\u54c8\u54c8\u54c8',存的是uncode
# print(type(s))#<type 'unicode'>
# print(s)#print 内部已经转换为unicode
# print(s.decode('utf-8'))#将字节 解码为unicode的,万国码

# s = '看看'
# s =s.encode('utf8')#b'\xe7\x9c\x8b\xe7\x9c\x8b' 这一步在py2里面已经乱码,py3这里是把unicode 编码为 bytes
# print(s)
# s = s.decode('utf8')#这一步 将bytes 解码为unicode
# print(s)
# # s = s.decode('gbk')#这一步 将utf8的bytes 解码为gbk则会出错,编码是utf8 解码接得使用utf8
# # print(s)

s = '解决'
s = bytes(s,'utf8')#py3 的字符串直接编码
print(s)
s = str(s,'utf8')#py3 的字符串直接解码
print(s)

# 要想保住程序 按照utf8来解析,文件本身保存格式必须为utf8
# 存储格式 必须 和编译格式 一致才能保住 编译成功