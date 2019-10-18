import csv

class GetData():
	def get_data(self,datapath):
		with open(datapath,'r') as f:
			readdata = csv.reader(f)
			#读标题
			head = next(readdata)
			username=[]
			passwd=[]
			for data in readdata:
				username.append(data[0])
				passwd.append(data[1])
		return head,username,passwd


# t=GetData()
# data=t.get_data(r'G:\AutoTest\data\userinfo.csv')
# print(data)
