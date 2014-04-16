# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd

# <codecell>

data = pd.read_csv('https://raw.github.com/pydata/pandas/master/pandas/tests/data/iris.csv')

# <codecell>

data

# <codecell>

# 1. How many different names of flowers are in this data set?
len(data.Name.unique())

# <codecell>

# 2. How many exist of each type of flower?
data.Name.value_counts()

# <codecell>

# 3. Determine the min, median, mean, max for each numeric feature in the data set.
data.describe()

# <codecell>

# 4. Determine the same for each flower type.
data.groupby(by='Name').describe()

# 5a. How does the shape of these results change from the average of all flowers?

#6b. Which features seem to be the most important in determining what kind of flower it is?
# Petal length and width have the biggest differences in mean value between different types of flowers.  

# <codecell>

# 7. Sort the data frame by each column (aside from Name), and print the results of each.
data.sort('SepalLength')

# <codecell>

data.sort('SepalWidth')

# <codecell>

print data.sort('PetalWidth', ascending=1)

# <codecell>

print data.sort('PetalLength', ascending=0)
# 7. What interesting trends exist in this data set, based on distributions?
## When sorting by Sepal size, the types of flower are somewhat mixed.
## They are almost de fact organized by type when using petal length

# <codecell>

#**8**. write several functions to apply to the data frame that attempt to organize the data set using 
#       strings instead of floats, like our short_or_long function from lecture. Use this to best 
#       summarize your data.
def classify_petal_length(x):
    return 'long' if x > data.mean().PetalLength else 'short'
    
def classify_petal_width(x):
    return 'wide' if x > data.mean().PetalWidth else 'narrow'
    
def classify_sepal_length(x):
    return 'long' if x > data.mean().SepalLength else 'short'
    
def classify_sepal_width(x):
    return 'wide' if x > data.mean().SepalWidth else 'narrow'

# <codecell>

data['Petal_Length_Class'] = data.PetalLength.apply(classify_petal_length)
data['Petal_Width_Class'] = data.PetalWidth.apply(classify_petal_width)
data['Sepal_Length_Class'] = data.SepalLength.apply(classify_sepal_length)
data['Sepal_Width_Class'] = data.SepalWidth.apply(classify_sepal_width)

# <codecell>

print data.groupby(['Name','Petal_Width_Class']).count().PetalWidth

# <codecell>

print data.groupby(['Name', 'Petal_Length_Class']).count().PetalLength

# <codecell>

print data.groupby(['Name','Sepal_Width_Class']).count().SepalWidth

# <codecell>

print data.groupby(['Name','Sepal_Length_Class']).count().SepalLength

# <codecell>
# 9. Attempted, but sort of trailed off
avg_lengths = data.groupby(by='Name').mean()['PetalLength']
print avg_lengths

# <codecell>

def compare_to_mean(value, feature, ftype):
    return abs(value - data[data.Name==ftype][feature].mean())

# <codecell>

#define list of features and flower types
features = ['PetalLength', 'PetalWidth', 'SepalLength', 'SepalWidth']
ftypes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# run compare_to_mean (comparing feature of one observation \
# to average of that feature for a specific flower type
print compare_to_mean(data.at[0,features[0]],features[0], ftypes[0])

# <codecell>

#define list of features and flower types
features = ['PetalLength', 'PetalWidth', 'SepalLength', 'SepalWidth']
ftypes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# run compare_to_mean (comparing feature of one observation \
# to average of that feature for a specific flower type

# <codecell>

data[49:51]

# <codecell>


