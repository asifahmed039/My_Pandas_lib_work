import pandas as pd
#shape and column
data={
    "name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print(df)
# print("descriptive statistics")
# print(df.describe())
print(f'shape:{df.shape}')  #give tuple (no of row,no_of_col)
print(f'Column Names:{df.columns}')  

"""
(10000,20)    large data set
(5,4)   small data set
"""