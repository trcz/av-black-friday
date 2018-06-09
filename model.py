import numpy as np
import pandas as pd
import xgboost as xgb

from sklearn.preprocessing import LabelEncoder

with open("train.csv", "rb") as myFile:
    train = pd.read_csv(myFile, delimiter=",")

with open("test.csv", "rb") as myFile:
    test = pd.read_csv(myFile, delimiter=",")


user_id_test = test['User_ID'].copy()
product_id_test = test['Product_ID'].copy()

le = LabelEncoder()
train['User_ID'] = le.fit_transform(train['User_ID'])
test['User_ID'] = le.transform(test['User_ID'])

#There were no new User_IDs in the test although there were 46 new Product_IDs

new_product_ids = list(set(pd.unique(test['Product_ID'])) - set(pd.unique(train['Product_ID'])))

le = LabelEncoder()
train['Product_ID'] = le.fit_transform(train['Product_ID'])
test.ix[test['Product_ID'].isin(new_product_ids), 'Product_ID'] = -1
new_product_ids.append(-1)

test.ix[~test['Product_ID'].isin(new_product_ids), 'Product_ID'] = le.transform(test.ix[~test['Product_ID'].isin(new_product_ids), 'Product_ID'])

pur_train = train['Purchase']
train.drop(['Purchase', 'Product_Category_2', 'Product_Category_3'], inplace=True, axis=1)
test.drop(['Product_Category_2', 'Product_Category_3'], inplace=True, axis=1)
train = pd.get_dummies(train)
test = pd.get_dummies(test)

dm_train = xgb.DMatrix(train.values, label=pur_train, missing=np.nan)

param = {'objective': 'reg:linear', 'booster': 'gbtree', 'silent': 1, 'max_depth': 10, 'eta': 0.1, 'nthread': 4, 'subsample': 0.8, 'colsample_bytree': 0.8, 'min_child_weight': 20, 'max_delta_step': 0, 'gamma': 0, 'seed': 2528}

round = 750

clf = xgb.train(param, dm_train, round)
dm_test = xgb.DMatrix(test.values, missing=np.nan)
predictions = clf.predict(dm_test)

submit = pd.DataFrame({'User_ID': user_id_test, 'Product_ID': product_id_test, 'Purchase': predictions})
submit = submit[['User_ID', 'Product_ID', 'Purchase']]
submit.to_csv("solution.csv", index=False)