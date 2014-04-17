1. 3 different names of flowers

2. 50 flowers each

3.        SepalLength  SepalWidth  PetalLength  PetalWidth
count   150.000000  150.000000   150.000000  150.000000
mean      5.843333    3.054000     3.758667    1.198667
std       0.828066    0.433594     1.764420    0.763161
min       4.300000    2.000000     1.000000    0.100000
25%       5.100000    2.800000     1.600000    0.300000
50%       5.800000    3.000000     4.350000    1.300000
75%       6.400000    3.300000     5.100000    1.800000
max       7.900000    4.400000     6.900000    2.500000

4.                        SepalLength  SepalWidth  PetalLength  PetalWidth
Name
Iris-setosa     count    50.000000   50.000000    50.000000   50.000000
                mean      5.006000    3.418000     1.464000    0.244000
                std       0.352490    0.381024     0.173511    0.107210
                min       4.300000    2.300000     1.000000    0.100000
                25%       4.800000    3.125000     1.400000    0.200000
                50%       5.000000    3.400000     1.500000    0.200000
                75%       5.200000    3.675000     1.575000    0.300000
                max       5.800000    4.400000     1.900000    0.600000
Iris-versicolor count    50.000000   50.000000    50.000000   50.000000
                mean      5.936000    2.770000     4.260000    1.326000
                std       0.516171    0.313798     0.469911    0.197753
                min       4.900000    2.000000     3.000000    1.000000
                25%       5.600000    2.525000     4.000000    1.200000
                50%       5.900000    2.800000     4.350000    1.300000
                75%       6.300000    3.000000     4.600000    1.500000
                max       7.000000    3.400000     5.100000    1.800000
Iris-virginica  count    50.000000   50.000000    50.000000   50.000000
                mean      6.588000    2.974000     5.552000    2.026000
                std       0.635880    0.322497     0.551895    0.274650
                min       4.900000    2.200000     4.500000    1.400000
                25%       6.225000    2.800000     5.100000    1.800000
                50%       6.500000    3.000000     5.550000    2.000000
                75%       6.900000    3.175000     5.875000    2.300000
                max       7.900000    3.800000     6.900000    2.500000

5. avg sepallength is lower for setosa, slightly higher for versicolor, significantly higher for virginica...
means are different for feature B, feature C, feature D...

6. Most Setosa flowers have a less than avg petal width and a greater than average sepal width.

7. Sorted by SepalLength, there are more setosa at the lower end and more virginica at the higher end. Sorted by SepalWidth, there are more versicolor
and virginica at the lower end and more versicolor/virginca at the higher end... you get the idea... print data.sort('SepalLength').values, etc.

8. Was working on something to the effect of:
def get_lg_than_avg(feature1, feature2):
	print data[(data[feature1] > data[feature1].sum() / len(data)][feature2].mean()
...the idea being the function would return the mean of feature2 for observations having a feature1 > the avg feature1.
...this is missing tests for null, etc and I don't think I got the syntax quite right. A for effort?
