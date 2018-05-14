# black-friday-eda

My attempt on https://datahack.analyticsvidhya.com/contest/black-friday/  
  
I will start with exploratory data analysis
  
  
**Dataset overview**  
  
| Column name | Values | Unique | Type |
| --- | --- | --- | --- |
| User_ID | 550068 | 5891 | non-null int64 |
| Product_ID | 550068 | 3631 | non-null object |
| Gender | 550068 | 2 | non-null object |
| Age | 550068 | 7 | non-null object |
| Occupation | 550068 | 21 | non-null int64 |
| City_Category | 550068 | 3 | non-null object |
| Stay_In_Current_City_Years | 550068 | 5 | non-null object |
| Marital_Status | 550068 | 2 | non-null int64 |
| Product_Category_1 | 550068 | 20 | non-null int64 |
| Product_Category_2 | 376430 | 17 | non-null float64 |
| Product_Category_3 | 166821 | 15 | non-null float64 |
| Purchase | 550068 | 18105 | non-null int64 |

Total number of records is 550068. Missing values occur in product categories 2 and 3. As we can see there are only 5891 unique users, 7 age categories and 20 product categories.  
I will focus at Purchase column first.  
  
Purchase is the only continous variable in the set while the rest is categorical.
