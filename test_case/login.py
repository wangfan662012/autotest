from selenium import webdriver
from test_case.public import *

class Login():
	def login(self):
		print('start login')
		driver=webdriver.Firefox(executable_path='E:/pycharm/geckodriver.exe')
		driver.get('https://www.baidu.com')
		t = get_data.GetData()
		head,ulist,plist=t.get_data(r'G:\AutoTest\data\userinfo.csv')
		print(ulist,plist)
		for username,passwd in zip(ulist,plist):
			driver.find_element_by_id('kw').send_keys(username)
			driver.find_element_by_id('kww').send_keys(passwd)
			driver.find_element_by_id('su').click()
			assert '登录成功'
			driver.find_element_by_id('exit').click()

