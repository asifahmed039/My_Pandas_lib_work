
import pandas as pd
data={
    "time":[1,2,3,4,5],
    "value":[10,None,30,None,50]
}

df=pd.DataFrame(data)
print("Before interpolation")
print(df)
print("After interpolation")
df['value']=df["value"].interpolate(method="linear")
print(df)