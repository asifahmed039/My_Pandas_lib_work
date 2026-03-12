#
import pandas as pd

data={
    "name":['Ram',None,'Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,None,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print(df)
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Salary'].fillna(df['Salary'].mean(),inplace=True)
print(df)
"""     
interpolate:- Wih the help of interpolate we insert the estimated value.
  only for numbric value
    10
    20
    nan
    40
    50 
    Algo:-
    linear interpolation
    1-preserve data integrity
    2-smooth trends
    3-avoid data loss

    interpolate()
    
"""
