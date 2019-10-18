import pytest
import pytest_html
import os,time
from py._xmlgen import html

now= time.strftime('%Y%m%d%H%M%S',time.localtime())
filename=r'G:\AutoTest\report\\' +now+ 'result.html'
wfile=open(filename,'wb')


# def run():
# 	os.system('pytest -v -s test_case/ --html=wfile')
# run()

if __name__ == '__main__':
	pytest.main(['-v', '-s', 'test_case/','--html=wfile'])
	pytest_html