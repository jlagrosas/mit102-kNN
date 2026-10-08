# Sample implementation to calculate for distances from a sample point to all entries in a dataset using Euclidian Distance
# author: lagrosas.jessiechristophere@gmail.com
# for: MIT 102 - kNN activity

import numpy as np
import pandas as pd

# read the dataset
df = pd.read_csv("data/iris.csv")
print(df)

# hard coded sample, should be modified to get input from user
sample = np.array([
    3.1,        # sepal_length
    1.2,        # sepal_width
    4.3,        # petal_length
    1.2,        # petal_width
])

# hard coded k, should be modified to get input from user
k = 7

df["distance"] = np.sqrt(
    (df["sepal_length"] - sample[0]) ** 2 + (df["sepal_width"] - sample[1]) ** 2  +
    (df["petal_length"] - sample[2]) ** 2 + (df["petal_width"] - sample[3]) ** 2
)

# remove the sample from df
df = df[df["distance"]>0]

df_sorted = df.sort_values("distance")

neighbors = df_sorted.head(k)

print(df)
print(df_sorted)
print(f"The nearest k neighbors are: ")

# Features used for kNN
features = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]

print(neighbors)

# count number of items for each specie
votes = neighbors["species"].value_counts()

# count the highest number of votes
prediction = votes.idxmax()

# display sample (input)
print(f"Sample input: ")
print(f"sepal_length = {sample[0]} ")
print(f"sepal_width = {sample[1]} ")
print(f"petal_length = {sample[2]} ")
print(f"petal_width = {sample[3]} ")
print(f"k = {k}")
print(f"The predicted specie is: {prediction}")
