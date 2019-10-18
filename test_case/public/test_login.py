from selenium import webdriver
import sys


class TestLogin():
	def setup_class(self):
		print('初始化浏览器')
		self.geckodriver = 'E:/pycharm/geckodriver.exe'
		self.driver = webdriver.Firefox(executable_path=self.geckodriver)
		self.driver.implicitly_wait(10)
		self.driver.maximize_window()
		self.url='https://www.baidu.com'
		self.datapath= ''

	def teardown_class(self):
		self.driver.quit()
		print('关闭浏览器')

	def get_data(self):
		with open(r'G:\AutoTest\data\userinfo.csv', 'r') as datafile:
			data = datafile.readlines()
			datafile.close()
			for line in data:
				line= line.strip('\n')
				li = line.split(' ')
				username = [li[0]]
				passwd = [li[1]]
				print(username, passwd)
		return username, passwd


	def test_login(self):
		print('start login')
		#driver = self.driver
		driver=webdriver.Firefox(executable_path='E:/pycharm/geckodriver.exe')
		#driver.get(self.url)
		driver.get('https://www.baidu.com')
		t=TestLogin.get_data()
		for username,passwd in t:
			driver.find_element_by_id('kw').send_keys(username)
			driver.find_element_by_id('kww').send_keys(passwd)
			driver.find_element_by_id('su').click()
			assert '登录成功'
			driver.find_element_by_id('exit').click()

