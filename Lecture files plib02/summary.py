"""
            df['column name'].mean()
            df['column name'].max()
            df['column name'].sum()
            df['column name'].mean()
"""""

import pandas as pd
data={
    "name":['Arun','Varun','Karan'],
    "Age":[28,34,22],
    "Salary":[1000,2000,3000]

}
df=pd.DataFrame(data)
average_salary=df['Salary'].mean()
print(average_salary)