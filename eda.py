import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

with open("train.csv", "rb") as myFile:
    df = pd.read_csv(myFile, delimiter=",")

print(df.shape)
print(df.info())
print(df.head())
#Removing missing values

df2 = df.drop(columns=["Product_Category_2", "Product_Category_3"])
print(df2.shape)
print(df2.info())

print(df2["Purchase"].describe())

plt.figure(figsize=(9, 8))
sns.distplot(df2["Purchase"], color="b")
plt.savefig("1.png")

print(df2.dtypes)
df_num = df2.select_dtypes(include = ["float64", "int64"]).drop(columns=["User_ID", "Purchase"])
print(df_num.shape)
print(df_num.info())

df_num.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)
plt.savefig("2.png")
