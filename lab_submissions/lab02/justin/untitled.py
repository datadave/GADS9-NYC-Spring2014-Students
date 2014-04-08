class Car():
	def __init__(self, model='Ford', wheels=4):
		self.model = model
		self.running = False
		self.wheels = wheels
	def start(self):
		if self.running != True:
			print 'The car started!'
			self.running = True
		else:
			print 'The car is already running!'
	def stop(self):
		if self.running == True:
			print 'The car stopped!'
			self.running = False
		else:
			print 'The car was not running!'