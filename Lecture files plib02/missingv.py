#How to handle the missing values.
"""
    NAN (not a number)
    None (for object data types)
            is null()
             True-NaN is missing
             False value is present
"""
import pandas as pd

data={
    "name":['Ram',None,'Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,None,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())

