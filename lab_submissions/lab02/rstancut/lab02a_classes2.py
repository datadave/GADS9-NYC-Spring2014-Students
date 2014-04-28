# create class 'Car'
class Car():
	# initiate class 'self' w/'model' and 'wheels' set to Ford and 4, respectively.
	def __init__(self, model='Ford', wheels=4):
		self.model = model
		self.running = False
		self.wheels = wheels
		# Car wheel check; sets count to zero if negative wheel count given.
		if self.wheels < 0:
			print 'The car cannot have negative wheels!'
			self.wheels = 0
			print 'The wheels have been set to zero.'
		else:
			print 'The car has %s wheels.' % self.wheels
	
	# Car 'start' function, deals w/car on or off.
	def start(self):
		if self.running != True:
			print 'The car started!'
			self.running = True
		else:
			print 'The car is already running!'

	# Car 'stop' function, deals w/car on or off.	
	def stop(self):
		if self.running == True:
			print 'The car stopped!'
			self.running = False
		else:
			print 'The car was not running!'
	


# assign class 'Car' to var 'ford'			
ford = Car()

# assign class 'Car' to var 'nissan' with new model and wheel attributes
nissan = Car(model = 'Nissan', wheels = -3)

# print wheel count on 'nissan'
print 'The Nissan car has %s wheels.' % nissan.wheels

# check 'running' status; should be False
ford.running

# run 'start' function on 'ford'
ford.start()

# check 'running' status; should be True
ford.running

# prints how many wheels on Ford.
print 'The Ford car has %s wheels.' % ford.wheels

# check 'running' status; should be False
nissan.running

# run 'stop' function on 'nissan'
nissan.stop()