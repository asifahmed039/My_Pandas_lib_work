import pandas as pd
data={
    'country_name':['India','china','Russia','USA','Iran'],
    'power_ful':[8,9,10,10,12],
    "Area":[7,6,1,3,10]
}

df=pd.DataFrame(data)
df.to_csv("prac.cvs")
# print(df)# print(df.info())
# print(df.head(3))
# print(df.tail(2))
print(df.columns)