Answers

************************

# assuming that it has been loaded into 'iris'

1. 3 diff names, len(iris.Name.unique())
2. 50 each, iris.name.value_counts()
3. iris.describe()
4. iris.groupby(by='Name').describe()
5a, 6b. The shape changes as we have a distribution by name (which is very different from the original averages). looks like PetalLength and PetalWidth are the most relevant due to the different means and low standard deviations
7. iris.sort('column').head(10) and so and so. pretty much what you expect from the mean.
8. using the averages from PetalLength, we used the middle point between the averages to make three buckets. Thus the function below:

def shortLong (x) :
    if x['PetalLength'] < 2.862:
        return 'Iris-setosa'
    elif x['PetalLength'] < 4.906:
        return 'Iris-versicolor'
    else:
        return 'Iris-virginica'

9. Looks like the one above gets 142/150! could probably do better with using PetalWidth as well!

