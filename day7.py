
print('day7-三级联动-编码/解码')
#ASCII 只能存英文和拉丁字符  一个字符占一个字节 8bit

#in python2 默认为ASCII
#gbk->UTF-8:先decode为unicode,然后由unikode转为utf-8

#in python3 文件默认为utf-8,python内部解析默认为unicode(编码之间转换,必须先转换为万国码(unicode),再向指定编码转换)
import sys
print(sys.getdefaultencoding()) #获取文件默认编码(utf-8)
s= 'i am 横说竖说';
print(s)
s_to_gbk = s.encode('gbk') #encode 在编码的提示会把ASCII外的字符 转换为bytes类型(注意python2里的的encode只是单纯的解码,python3里的解码会在解码的同时将其转为字节->bytes)
print(s_to_gbk) #:b'i am \xba\xe1\xcb\xb5\xca\xfa\xcb\xb5' (b=byte 字节类型)
#unicode_to_gbk = s_to_unicode.encode('gbk')
gbk_to_gbk = s_to_gbk.decode('gbk') #将 字节类型以gbk方式解码
print(gbk_to_gbk)