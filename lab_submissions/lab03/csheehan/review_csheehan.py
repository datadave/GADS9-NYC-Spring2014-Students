#1. What's the data type of `[1, 2, 3]` ?
x = [1,2,3]
print type(x)
#<type 'list'>

#2. What's `'yellow' + '_' + 'orange'`?
print 'yellow' + '_' + 'orange'
#yellow_orange

#3. What's `2 / 5`? How about `float(2) / float(5)`?
print 2/5
# 0
print float(2)/float(5)
# 0.4

import datetime
tweet = {
    'date': datetime.datetime(2014, 4, 1, 23, 14, 20),
    'user': 899110,
    'text': '<3 OMG BEST FRIENDS ARE THE BEST #bestiesforlife #oclove',
    'location' : {
        'lat': 27.0,
        'lng': 114.9,
        'hex': 'Efabe3'
    }
}

#4. What's the data type of 'tweet'?
print type(tweet)
#<type 'dict'>

#5. What's the data type of 'date'?
print type(tweet['date'])
#<type 'datetime.datetime'>

#6. How would you print the 'text' of the above tweet?
print tweet['text']

#7. Calculate the average the following object:
some_values = [100, 107.7, 92]
avg = sum(some_values)/len(some_values)
print avg
# 99.9

#8. write a function that takes a list as an argument and returns back the average of that list.
def get_avg(list):
	return sum(list)/len(list)

#Use the following code to work through problems 9-12
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[1, 2], [3, 4], [5,6]])

#9. What happens if you do `a * b`?
print a*b
#Check the help function of np.dot(). (run `help(np.dot())`)
help(np.dot)
#10. Why does `a.dot(b)` fail? Why does `a.dot(c)` work?
#The number of dimensions in b do not match the number of values in a (3)	

#11. Is `np.dot(a, c)` the same as `a.dot(c)`? Why or why not?
print np.dot(a,c)
print a.dot(c)
# Yes, different ways of doing the same function

#12. Is `np.dot(a, c)` the same as `np.dot(c, a)`? Why or why not?
print np.dot(a,c)
print np.dot(c,a)
# No, one multiplies a through c, the other a through c
