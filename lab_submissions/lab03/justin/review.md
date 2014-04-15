## Python Data Review

In a text file, have the answers to the following questions. Feel free to use a python interpreter to work:

python
ipython
ipython notebook

1. What's the data type of `[1, 2, 3]` ?
list

2. What's `'yellow' + '_' + 'orange'`?
sting, 'yellow_orange'

3. What's `2 / 5`? How about `float(2) / float(5)`?
0
0.4

Use the following code to work through problems 4-6
```python
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
```

4. What's the data type of 'tweet'?
library

5. What's the data type of 'date'?
datetime

6. How would you print the 'text' of the above tweet?
print tweet['text']

7. Calculate the average the following object:

```python
some_values = [100, 107.7, 92]
```
print sum(some_values) / len(some_values)
round(sum(some_values) / len(some_values), 1)


8. write a function that takes a list as an argument and returns back the average of that list.

def mean(s):
	return sum(s) / len(s)


Use the following code to work through problems 9-12
```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[1, 2], [3, 4], [5,6]])

```
9. What happens if you do `a * b`?
Check the help function of np.dot(). (run `help(np.dot())`)

multiplies corresponding values in the 2d array

10. Why does `a.dot(b)` fail? Why does `a.dot(c)` work?
not sure

11. Is `np.dot(a, c)` the same as `a.dot(c)`? Why or why not?
yes

12. Is `np.dot(a, c)` the same as `np.dot(c, a)`? Why or why not?
no
