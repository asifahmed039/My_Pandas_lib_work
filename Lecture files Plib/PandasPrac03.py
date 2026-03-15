import pandas as pd
data={
    'country_name':['India','china','Russia','USA','Iran'],
    'power_ful':[8,9,10,10,12],
    "Area":[7,6,1,3,10]
}

df=pd.DataFrame(data)
print(df[df['Area']>3])
