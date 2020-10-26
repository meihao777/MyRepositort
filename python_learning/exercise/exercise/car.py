class Car():
	'''一次模拟汽车的简单尝试'''

	def __init__(self,make,model,year):
		'''初始化汽车属性'''
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 2048

	def get_descriptive_name(self):
		'''返回整洁的描述性信息'''
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		'''打印一条指出汽车里程的消息'''
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,mileage):
		'''将里程表数设为特定的值
			禁止任何人回调里程表数'''
		if self.odometer_reading > mileage:
			print("You can't roll back an odometer!")
		else:
			self.odometer_reading = mileage
	def increment_odometer(self,mileage):
		'''将里程表增加一定的里程数'''
		if mileage < 0:
			print("You can't roll back an odometer!")
		else:
			self.odometer_reading+=mileage

