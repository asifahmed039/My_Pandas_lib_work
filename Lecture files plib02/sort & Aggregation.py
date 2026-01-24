#Sorting data
""""
     sorting data 1 column sort_values()

     df.sort_values(by="col_name",true/false,inplace=True)

     true for ascending
     false for descending

"""
import pandas as pd
data={
    "name":['Arun','Varun','Karan'],
    "Age":[28,34,22],
    "Salary":[1000,2000,3000]

}
df=pd.DataFrame(data)
df.sort_values(by='Age',ascending=False, inplace=True)
print('sorting age by descending')
print(df)
