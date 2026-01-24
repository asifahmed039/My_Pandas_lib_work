import pandas as pd

data={
    "name":['Arun','Varun','Karun','Narun','Marun'],
    "Age":[28,34,22,34,28],
    "Salary":[50000,60000,45000,52000,48000]

}
df=pd.DataFrame(data)
grouped=df.groupby('Age')['Salary'].sum()
                #group    aggregation
print(grouped)
group=df.groupby(['Age','name'])['Salary'].max()
print(group)