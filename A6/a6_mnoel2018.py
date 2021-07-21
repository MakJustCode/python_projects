# Reading the data from the irirs.csv file

import seaborn as sns

iris = sns.load_dataset('iris')

iris.head()

# Computing minimum, maximum, mean, standard deviation and some other statistical information for out dataset

iris.describe()

# Plotting scatter plots between sepal width vs. sepal length

import matplotlib.pyplot as plt

plt.scatter(iris["sepal_width"],iris["sepal_length"])

plt.show()

# Plotting scatter plots between petal width vs. petal length

import matplotlib.pyplot as plt

plt.scatter(iris["petal_width"],iris["petal_length"])

plt.show()

# Normalising the data

iris["sepal_length"]=iris["sepal_length"]/iris["sepal_length"].max()

# Normalising the data

iris["sepal_width"]=iris["sepal_width"]/iris["sepal_width"].max()

# Normalising the data

iris["petal_length"]=iris["petal_length"]/iris["petal_length"].max()

# Normalising the data

iris["petal_width"]=iris["petal_width"]/iris["petal_width"].max()

iris.head()