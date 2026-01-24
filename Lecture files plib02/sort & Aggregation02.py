#sorting on multiple column
import pandas as pd
data={
    "name":['Arun','Varun','Karan'],
    "Age":[28,34,22],
    "Salary":[1000,2000,3000]

}
df=pd.DataFrame(data)
df.sort_values(by=['Age','Salary'],ascending=[True,False], inplace=True)
print('sorting age by descending')
print(df)
