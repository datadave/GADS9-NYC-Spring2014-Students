# define class Car
class Car():
	#define initiation function for class with default values for model and wheels
	def __init__(self, model='Ford', wheels = 4):
		#assign object attribute 'model' as defined in object declaration, or default "Ford"
		self.model = model
		#assign object attribute 'running' to False
		self.running = False
		# if less than zero wheels on car, throw error
		if wheels < 0:
			raise Exception("Too few wheels")
		# else, set object attribute 'wheels' as defined in object declaration, or default 4		
		else:
			self.wheels = wheels
	#define function start to start vehicle
	def start(self):
		# if vehicle is not currently running, print that car is started and set its attribute "running" as True
		if self.running != True:
			print 'The car started!'
			self.running = True
		# else, print that car is already running	    
		else:
			print 'The car is already running!'
	def stop(self):
		# if vehicle is currently running, print that car is stopped and set its attribute "running" as False
		if self.running == True:
			print 'The car stopped!'
			self.running = False
		# else, print that car is already stopped
    		else:
			print 'The car was not running!'