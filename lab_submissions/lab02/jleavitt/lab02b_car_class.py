class Car():  # Define Car
    def __init__(self, model='Ford', wheels=4):   # Initialize by default as 4-wheel Ford
        self.model = model	# self.model string set to 'Ford' or entered model
        self.running = False	# self.running boolean initially set to False
        if wheels < 0:	# Test for negative wheels (a common automotive defect)			
            print 'Your car has negative wheels? What the hell? Resetting to 0.'
            wheels = 0	# Corrects problem
        elif wheels < 4:
            print 'You do realize your car has fewer than 4 wheels? Where are you going to go on %i wheels?' % wheels 	# prints out snarky comment
        self.wheels = wheels	# Subtly different due to relation to Car class
    def start(self):		# Defines function for items in Car class
        if self.running != True:	# Tests that car is not already running
            print 'The car started!'
            self.running = True		# If not, starts it
        else:
            print 'The car is already running!'
    def stop(self):
        if self.running == True:	# Tests that car is running
            print 'The car stopped!'
            self.running = False	# Stops all that
        else:
            print 'The car was not running!'

# Below are some commands to run declaring or using items of class Car

ford = Car()
nissan = Car(model = 'Nissan')
ford.running
ford.start()
ford.stop()
nissan.running
nissan.stop()
ford = Car(wheels = 4)
ford.stop()
car was not running!
toyota = Car(wheels=3)
toyota = Car(wheels=-2)
