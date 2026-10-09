# Sample implementation to calculate for distances from a sample point to all entries in a dataset using Euclidian Distance
# author: lagrosas.jessiechristophere@gmail.com
# for: MIT 102 - kNN activity

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### INPUTS
INPUT_CSV="data/iris.csv"
INPUT_SAMPLE="data/input.txt"
INPUT_K="data/k.txt"


# read the dataset
df = pd.read_csv(INPUT_CSV)
print("The input dataset:")
print(df)

# read sample data
sample = []
with open(INPUT_SAMPLE, "r") as file:
    for line in file:
        
        value = line.split("#")[0].strip()
        if value:
            sample.append(float(value))

# convert sample to np array
sample = np.array(sample)

print(f"Sample:")
print(sample)
print(f"Len sample:", len(sample)) 

# read value of k
with open(INPUT_K, "r") as file:
    k = int(file.read().strip())


## calculating for the distance to each entry in dataset against sample
## add a field "distance" to the dataframe
df["distance"] = np.sqrt(
    (df["sepal_length"] - sample[0]) ** 2 + (df["sepal_width"] - sample[1]) ** 2  +
    (df["petal_length"] - sample[2]) ** 2 + (df["petal_width"] - sample[3]) ** 2
)

# remove the sample from df
df = df[df["distance"]>0]
# sort according to "distance"
df_sorted = df.sort_values("distance")
# the top k are the nearest neighbors
neighbors = df_sorted.head(k)

print(f"The nearest k neighbors are: ")
print(neighbors)

# Features used for kNN
features = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]

# count number of items for each specie
votes = neighbors["species"].value_counts()

# count the highest number of votes, which specie has the most number
prediction = votes.idxmax()

# display sample (input)
print(f"Sample input: ")
print(f"sepal_length = {sample[0]} ")
print(f"sepal_width = {sample[1]} ")
print(f"petal_length = {sample[2]} ")
print(f"petal_width = {sample[3]} ")
print(f"k = {k}")
print(f"The predicted specie is: {prediction}")


# attempt the display graph using matplotlib
plt.figure()

# add more colors when needed, in case there are more than (6) species
colors = ["red", "green", "blue", "cyan", "gray", "purple"]

## plotting the dataset
## retrieve all unique species 
species_list = df["species"].unique()

# for each unique species, plot based on colors
for i, species in enumerate(species_list): 

    species_data = df[df["species"] == species]

    # using only the petal_length and petal_width to plot the dataset
    plt.scatter(
        species_data["petal_length"],
        species_data["petal_width"],
        label=species,                  # legends
        alpha=0.7,                      # opacity
        color=colors[i]
    )


for _, neighbor in neighbors.iterrows():

    plt.plot(
        [sample[2], neighbor["petal_length"]],
        [sample[3], neighbor["petal_width"]],
        linestyle="--",
        linewidth=1
    )

print(neighbors)
## plotting the nearest neighbors
plt.scatter(
    neighbors["petal_length"],
    neighbors["petal_width"],
    s=70,
    facecolors="none",
    edgecolors="black",
    linewidths=1.5,
    label="Nearest Neighbors"
)

## plotting the given sample
plt.scatter(
    sample[2],                  # using petal_length
    sample[3],                  # using petal_width
    s=100,
    marker="o",
    color="yellow",
    edgecolors="black",
    linewidths=2,
    label="New Sample"
)

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.title(
    f"kNN Classification (k = {k})\n"
    f"Predicted Class: {prediction}"
)

plt.legend()

plt.grid(alpha=0.2)
plt.show()
