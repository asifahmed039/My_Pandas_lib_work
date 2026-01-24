import pandas as pd


import pandas as pd

data={
    "name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
# df.loc[1,'Salary']=70000
print(df)

# print(df.isnull().sum())
# # df['Age'].fillna(df['Age'].max(),inplace=True)
# df['Age'].interpolate(method='linear',axis=0,inplace=True)
# print(df)

df.sort_values(by='Age',ascending=False,inplace=True)
print(df)




 