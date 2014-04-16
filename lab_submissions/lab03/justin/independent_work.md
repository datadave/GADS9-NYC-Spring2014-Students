## PANDAS Practice

Load the `iris` data set from the web using this url.
`https://raw.github.com/pydata/pandas/master/pandas/tests/data/iris.csv`

The iris data set is well known, learn more about it <a href="http://en.wikipedia.org/wiki/Iris_flower_data_set">here</a>!

Answer the following questions using python, numpy, and pandas.

1. How many different names of flowers are in this data set?
3

2. How many exist of each type of flower?
50 each

3. Determine the min, median, mean, max for each numeric feature in the data set.
data.min()
data.median()
data.mean()
data.max()

SepalLength:
	min: 4.3
	median: 5.8
	mean: 5.84
	max: 7.9

SepalWidth:
	min: 2.0
	median: 3
	mean: 3.05
	max: 4.4

PetalLength:
	min: 1
	median: 4.35
	mean: 3.76
	max: 6.9

PetalWidth:
	min: 0.1
	median: 1.3
	mean: 1.2
	max: 2.5

4. Determine the same for each flower type.
Iris-setosa
min
SepalLength	4.3
SepalWidth	2.3
PetalLength	1.0
PetalWidth	0.1
median
SepalLength	5.0
SepalWidth	3.4
PetalLength	1.5
PetalWidth	0.2
mean
SepalLength	5.006
SepalWidth	3.418
PetalLength	1.464
PetalWidth	0.244
max
SepalLength	5.8
SepalWidth	4.4
PetalLength	1.9
PetalWidth	0.6

Iris-versicolor
min
SepalLength    4.9
SepalWidth     2.0
PetalLength    3.0
PetalWidth     1.0
median
SepalLength    5.90
SepalWidth     2.80
PetalLength    4.35
PetalWidth     1.30
mean
SepalLength    5.936
SepalWidth     2.770
PetalLength    4.260
PetalWidth     1.326
max
SepalLength    7.0
SepalWidth     3.4
PetalLength    5.1
PetalWidth     1.8

Iris-virginica
min
SepalLength    4.9
SepalWidth     2.2
PetalLength    4.5
PetalWidth     1.4
median
SepalLength    6.50
SepalWidth     3.00
PetalLength    5.55
PetalWidth     2.00
mean
SepalLength    6.588
SepalWidth     2.974
PetalLength    5.552
PetalWidth     2.026
max
SepalLengt      7.9
SepalWidth      3.8
PetalLength     6.9
PetalWidth      2.5

5a. How does the shape of these results change from the average of all flowers?
not sure

6b. Which features seem to be the most important in determining what kind of flower it is?

Setosa's have smaller petals
Others I'm not sure


7. Sort the data frame by each column (aside from Name), and print the results of each. What interesting trends exist in this data set, based on distributions?
Setosa's have the smallest petal width and lengths, as well as sepal lengths, but longest sepal widths
Versicolor's look to be approximately (quick guess from scanning data) twice as likely to have a small sepal width

**8**. write several functions to apply to the data frame that attempt to organize the data set using strings instead of floats, like our short_or_long function from lecture. Use this to best summarize your data.

**9**. CHALLENGE QUESTION: From everything above, you should be able to predict relatively accurately for each row what kind of flower it is (without using the Name column as an obvious hint). Write a function that uses the data with if and else statements to attempt to classify each row.
