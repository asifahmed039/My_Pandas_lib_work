#[01] Explore the data set carefully.
"""
    (01)Understand the data set.
    (02)Identify the problems.
    (03)Plan next steps.

    tail() and head() are use to print the last and first sub data of data set.
    bydefault 5 data print.

    (01)Column,Row in data set.
    (02)What type of data?
    (03)Missing Data in data set.

        info()    #method
            This mehtods gives :----
            (01)Number of rows and column.
            (02)Column name
            (03)int64  float64 and object
            (04)memory usage of the data frame 
            (05)non null counts 
                        details on file 05P.py 
"""
import pandas as pd
df=pd.read_json('My_Pandas_Work\Lecture files Plib\sample_Data.json')
# print(df)
print('print first 10 rows of data set.')
print(df.head(10))
#tail
print('display last 10 rows of data set.')
print(df.tail(10))

