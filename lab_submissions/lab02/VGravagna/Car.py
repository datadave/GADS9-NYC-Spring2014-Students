class Car():
    #constructor
    def __init__(self, model='Ford', wheels=4):
        #setting defaults
        self.model = model
        self.running = False
        self.wheels = wheels
        #if wheels is negative set to zero
        if self.wheels < 0:
       		print "You can't have negative wheels on a car."
       		self.wheels = 0
    #function to start car
    def start(self):
        if self.running != True:
            print 'The car started!'
            self.running = True
        else:
            print 'The car is already running!'
    #function to stop car
    def stop(self):
        if self.running == True:
            print 'The car stopped!'
            self.running = False
        else:
            print 'The car was not running!'

#Sample class variable assignments and function calls
ford = Car()
nissan = Car(model = 'Nissan')
ford.running
ford.start()    #The car started!
ford.running
nissan.running
nissan.stop()   #The car was not running!

merc = Car('Mercedes', -2)  #You can't have negative wheels on a car.
merc.start()    #The car started!
bent = Car('Bentley')
bent.start()    #The car started!
