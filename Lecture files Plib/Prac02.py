import pandas as pd
# df=pd.read_excel('My_Pandas_Work\Lecture files Plib\SampleSuperstore.xlsx')
# print(df.head(10))
# print(df.info())
# print(df.describe())
# print(f'shape:{df.columns}')



data={
    "name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
# names=df[['name','Age']]
names=df[(df['Age']>25 ) & (df['Salary']>50000)]
print(names)





