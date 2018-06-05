import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

with open("train.csv", "rb") as myFile:
    df = pd.read_csv(myFile, delimiter=",")

print(df.info())
print(df.nunique())
plt.figure(figsize=(9, 8))

#creating Purchase variable distribution plot and saving it as 1.png
sns.distplot(df["Purchase"], color="b")
plt.savefig("1.png")

#dropping unnecessary columns from dataframe
df2 = df.drop(columns=["User_ID", "Product_ID", "Product_Category_2", "Product_Category_3", "Purchase"])

fig, axes = plt.subplots(round(len(df2.columns) / 3), 3, figsize=(18, 12))

#creating countplots for categorical variables and saving it as 2.png
for i, ax in enumerate(fig.axes):
    if i < len(df2.columns):
        ax.set_xticklabels(ax.xaxis.get_majorticklabels(), rotation=45)
        sns.countplot(x=df2.columns[i], alpha=0.7, data=df2, ax=ax, order=sorted(df2[df2.columns[i]].unique()))
plt.savefig("2.png")

plotnames = df.columns.values.tolist()
toDrop = ["User_ID", "Product_ID", "Purchase"]
plotnames = [x for x in plotnames if x not in toDrop]

for i in plotnames:
    plt.figure(figsize=(10, 6))
    ax = sns.boxplot(x=i, y='Purchase', data=df, order=sorted(df[i].unique()))
    plt.setp(ax.artists, alpha=.5, linewidth=2, edgecolor="k")
    plt.xticks(rotation=45)
    plt.savefig(i+".png")
