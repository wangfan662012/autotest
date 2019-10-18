from selenium import webdriver
import time
import pytest

class TestSearch():

	def setup_method(self):
		print("初始化浏览器")
		geckodriver = 'E:/pycharm/geckodriver.exe'
		self.driver = webdriver.Firefox(executable_path=geckodriver)
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.url ='https://www.baidu.com'
		self.datapath = r'G:\AutoTest\data\searchinfo.txt'

	def teardown_method(self):
		self.driver.quit()
		print("关闭浏览器")

	def getdata(self):
		with open(self.datapath, 'r') as datafile:
			data = datafile.readlines()
			datafile.close()
			info=[]
			for line in data:
				line = line.strip('\n')
				info.append(line)
		return info

	def test_baidu(self):
		info=TestSearch.getdata(self)
		for one in info:
			self.driver.get(self.url)
			self.driver.find_element_by_id("kw").send_keys(one)
			time.sleep(2)
			self.driver.find_element_by_id("su").click()
			print("打开浏览器搜索: %s" % one)
			time.sleep(2)


# if __name__ == "__main__":
# 	t=TestSearch()
# 	print(t.get_data())