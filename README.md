# kNN Activity

## MIT 102 - Advanced Database Systems

A script to calculate for kNN by finding the similarity distance,

## Objectives:
- To apply kNN algorithm to a fisheriris dataset
- To identify similarity distance of the two data points in a given dataset by applying distance function
- To perform data analysis on fisheriris dataset

## Notes:
- Apply using the Euclidian distance of 2 data points

## Sample data

| sepal_length | sepal_width | petal_length | petal_width | species |
| :---         | :---        | :---         | :---        | :---    |
| 5.1          | 3.5         | 1.4          | 0.2         | setosa  |
| 4.9          | 3.0         | 1.4          | 0.2         | setosa  |
| 4.7          | 3.2         | 1.3          | 0.2         | setosa  |
|              |             |              |             |         |

## Prerequisites

1. Python (version used during the creation of this project: Python 3.14.8
2. Git 


## Project Directory Structure

```
mit102-kNN/
├── data/
│   ├── iris.csv
│   ├── input.txt
│   └── k.txt
├── src/
│   └── knn.py
├── requirements.txt
└── README.md
```

Data Files:
1. data/iris.csv
Contains the input dataset, downloaded from:
https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642 a06d3d5b9bcbad9890c8ee534/iris.csv

2. data/sample.txt
Contains values for the sample to be classified. Sample format:

```
5.1  # sepal_length
3.5  # sepal_width
6.0  # petal_length
2.0  # petal_width
```
3. data/k.txt
Contains the value for k. Sample format:

```
10
```

## Getting Started

Follow the following steps to install this project locally.

### 1. Clone the repository

### 2. Environment Setup

Create the environment for this project. The steps may differ on another OS, these steps worked on a mac_os.

#### Create the virtual environment

```
python3 -m venv .venv
```
#### Activate virtual environment

```
source .venv/bin/activate
```

#### Install requirements.txt

```
pip install -r requirement.txt
```

### 3. Usage

Modify the following files to reflect the sample to be classified:
1. data/sample.txt
2. data/k.txt


Then run the following:

```
python src/mit_102_4.py
```

## Resources

**Numpy**
Numpy is used to create the numerical array, and do numerical operations on them.

[Numpy Documentation](https://numpy.org/doc/stable/)

**Pandas**
Pandas is used for reading the input dataset (iris.csv).

[Pandas Iterrate Over Rows](https://www.datacamp.com/tutorial/pandas-iterate-over-rows?utm_cid=19589720824&utm_aid=157156376311&utm_campaign=230119_1-ps-other~dsa-tofu~all_2-b2c_3-apac_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9066991-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~apac-en~dsa~tofu~tutorial~python&gad_source=1&gad_campaignid=19589720824&gbraid=0AAAAADQ9WsGl_3jCr4I5myiKO8bGAzBhK)

[Pandas Documentation](https://pandas.pydata.org/docs/)

**Matplotlib**
Used to create the graph for display.

[Matplotlib](https://matplotlib.org/stable/api/index)
[matplotlib.pyplot.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter)

Matplotlib tutorials
    [matplotlib line, bar, scatter](https://www.datacamp.com/tutorial/matplotlib-tutorial-python?utm_cid=19589720824&utm_aid=157156376311&utm_campaign=230119_1-ps-other~dsa-tofu~all_2-b2c_3-apac_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9066905-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-other~apac-en~dsa~tofu~tutorial~python&gad_source=1&gad_campaignid=19589720824&gbraid=0AAAAADQ9WsFdVVtYaofcEeHmdt4Cf_AUG)

    
## Youtube videos

[kNN (k-Nearest Neighbors Algorithm) | Data Mining and Applications | SY 2020-2021](https://www.youtube.com/watch?v=iUDgdP19UhY)

[Solved Numerical Example of KNN Classifier to classify New Instance IRIS Example by Mahesh Huddar](https://www.youtube.com/watch?v=Vk9lGGODaJA)
 
