#update value at particular position

import pandas as pd

data={
    "name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
# print(df)
#.loc[]
#df.loc[row_index,"column name"]=new_value

df.loc[0,'Salary']=50000+(50000 * 0.1)
df.loc[0,'Performance Score']=90
print(df)


