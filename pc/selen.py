#__author: xlu.com
#date : 2018/8/12
from selenium import webdriver

# geckodriver.exe 下载dirver放在python的安装目录下后 可以不用指定扩展路径
driver_path = r'C:\dev\Python\Python35\geckodriver.exe'

driver = webdriver.Firefox(executable_path=driver_path)
driver.get('https://www.baidu.com')
el = driver.find_element_by_id('kw')
el.send_keys('python')

el = driver.find_element_by_id('su')
el.click()
# driver = webdriver.Firefox()
# webdriver.Chrome()
# driver.get('https://www.baidu.com')
# print(driver.page_source)
# driver.close() 关闭当前页面
# driver.quit() 退出浏览器