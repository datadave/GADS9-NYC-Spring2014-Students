s = 'hello world, world'
#replaces every instance of world with python
s2 = s.replace("world", "python")

#replaces every instance of hello with monty
s3 = s2.replace("Hello","monty")

#prints each variable
print s
print s2
print s3

#prints character 7 (6th index) though 11 (10th index)
print s[6:11]

#prints 7th and on
print s[6:]

#prints last two chars
print s[-2:]


#concats s with s3 and a space in between
s4 = s + ' ' + s3

print s4

#pulls first index of first char of 'world'
print s4.find('world')


#changes placeholders with corresponding values of format inputs
print 'A string with value {0} and {1}'.format(10,20.3)

#documentaion for type str
help(str)



########
# List
########


#defines list named values
values = ['1',2,3.0,False]

#prints the length of the list
print len(values)
# prints the type of the list
print type(values)

#prints the actual list
print values

#prints second value
print values[1]

#prints the first 3 values of list
print values[:3]

#prints 3rd value till the end
print values[2:]

# defines l as empty list
l = []

#adds each input to end of the list
l.append(8)
l.append(10)
l.append(10)
l.append(12)


print l

#removes first instance of 10
l.remove(10)
print l

#removes first value of list
l.remove(l[0])
print l


l = range(0,10,2)


print l
l = range(-5,5)
print l
line = "This is a    \t list -      \t of strings"

#print length of following list
print len(line.split('\t'))
##creates list separated by each \t
print line.split('\t')

#creates a list with string as an iteration (10 times)
print ['add another field' for i in range(10)]

#creates l ranging from -5 to 4
l = range(-5,5)

print l

#sorts it in reverse order
print l.sort(reverse=True)
print l

print "-----------\n\n\n CLASSES \n\n\n-------------"

class Car():
    def __init__(self, model='Ford',wheels = 4):
        self.model = model
        if wheels < 0:
        	#whats difference btw this and print
        	raise Exception('Need more wheels!')
        else:
        	self.wheels = wheels
        self.running = False
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
print 'test'
nissan = Car(model = 'Nissan')
ford.running
ford.start()
ford.running
nissan.running
nissan.stop()














