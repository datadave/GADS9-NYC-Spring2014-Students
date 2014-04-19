class Car():
    def __init__(self, model='Ford',wheels=4):
        self.model = model
        self.running = False
	if wheels <=0:
		print 'Wheels is less than or equal to 0'
	else:
		print 'Wheels is greater than 0'
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


#create a ford car.
ford = Car()
#create a nissan car model nissan, this replaces the ford default, replace wheels with a value of 0.
nissan = Car(model = 'Nissan',wheels=0)
#set ford to start off running.
ford.running
#start the class with ford.
ford.start()
#set ford to run.
ford.running
#set nissan to run.
nissan.running
#set nissan to stop.
nissan.stop()