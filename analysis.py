import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt


# load dataset
df = pd.read_csv("medium_dataset_1000.csv")

# dataset information
print(df.info())
print(df.shape)
print(df.describe())


# missing value analys
count_missing = (df.isnull().sum())
percentage_missing = 100 * (df.isnull().sum()) / len(df)
take_mix = pd.concat(
    [count_missing,percentage_missing],
    axis=1,
    keys=["count_missing","percentage_missing"]
)
print(take_mix)


# The most Practical methods in "missingno"
print(msno.matrix(df))          
print(msno.heatmap(df))
print(msno.bar(df))
print(msno.dendrogram(df))
plt.show()