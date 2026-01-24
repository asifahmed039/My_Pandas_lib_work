#Data modification
"""
    [01]Adding column

"""
import pandas as pd

data={
    "name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
#square brakcets df["column_name"]=some_data
df['bonus']=df['Salary'] * 0.1   #not freedom to add any position.
print(df)
#so use insert method 
# df.insert(loc,col_name,some_data)
df.insert(0,"employee_id",[101,102,103,104,105,106,107,108])
print(df)