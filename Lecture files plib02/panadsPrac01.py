

import pandas as pd

data={
    "name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
# print(df[(df['Age']>28) &(df['Salary']>50000)])
# df['bonus']=df['Salary']*0.1
# df.insert(0,"Emp_Id",[1001,1002,1003,1004,1005,1006,1007,1008])

df.insert(0,'emp_id',[2201,2202,2203,2204,2205,2206,2207,2208])
df.insert(5,'city',['Patna',"Patna",'Jehanabad','Hyderabad','Pune','Delhi','Delhi','Jehanabad',
                    ])

# print(df.head(5))
print(df['Salary'].min())
grouped=df.groupby('city')['Salary'].sum()
print(grouped)