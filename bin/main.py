
import sys,os
#绝对方式添加
#sys.path.append('E:\python_text')

#相对路径
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 导入模块儿
from model import logging
logging.log()