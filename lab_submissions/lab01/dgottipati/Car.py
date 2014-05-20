
# Creates a new Class for Car
class Car():

	""" This is the initialization of the Car class
	Defaults to the model = Ford; wheels = 4 """

	def __init__(self, model='Ford', wheels=4):
		self.model = model # assigning the model passed into class to model variable
		self.running = False # assigning the value of running to False, as the car is initially not running
		self.wheels = wheels # assigning the value of the wheels passed in to the wheels variable of the object

		"""This snippet checks to see if the wheeks are less than zero.
		 If the wheels are less than 0, it prints an error message and sets the wheels = 0 """
		if self.wheels < 0:
			print "You can't have negative wheels on a car."
			self.wheels = 0

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

ford = Car()
nissan = Car(model = 'Nissan', wheels=-2)
ford.running
ford.start()
ford.running
nissan.running
nissan.stop()

