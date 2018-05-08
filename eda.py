import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

with open("train.csv", "rb") as myFile:
    df = pd.read_csv(myFile, delimiter=",")

print(df.info())
print(df.nunique())
