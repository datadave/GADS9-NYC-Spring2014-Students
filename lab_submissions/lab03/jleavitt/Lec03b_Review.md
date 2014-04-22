1. What's the data type of [1, 2, 3] ?
It's a list (of integers).

2. What's 'yellow' + '_' + 'orange'?
A string = 'yellow_orange'

3. What's 2 / 5? How about float(2) / float(5)?
I might have expected the first one to be an integer, maybe rounded down to the floor of 0, but in fact when I type these in I get identical results: 0.4 and 0.4.

4. What's the data type of 'tweet'? 
Ans: it's a dictionary

5. What's the data type of 'date'?
Ans: datetime.datetime  (object type)

6. How would you print the 'text' of the above tweet? 
Ans: print ['text'] 

7. Calculate the average of the following object: some_values = [100, 107.7, 92]
Ans: 99.9

some_values = [100, 107.7, 92]
>>> sum(some_values)
299.7
>>> sum(some_values)/len(some_values)
99.89999999999999
>>> round(sum(some_values)/len(some_values),2)
99.9

8. write a function that takes a list as an argument and returns back the average of that list.
Use the following code to work through problems 9-12
Ans:

def mean(x):
	return sum(x)/ len(x)

mean (some_values)



9. What happens if you do a * b? Check the help function of np.dot(). (run help(np.dot()))
Ans: The matrices are multiplied together: 
array([[ 1,  4,  9],
       [16, 25, 36]])


10. Why does a.dot(b) fail? Why does a.dot(c) work?
Ans: They are not aligned? 
array([[22, 28],
       [49, 64]])

11. Is np.dot(a, c) the same as a.dot(c)? Why or why not?
Ans: Yes

12. Is np.dot(a, c) the same as np.dot(c, a)? Why or why not? 
No ... not sure. 
