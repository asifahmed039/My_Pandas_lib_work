"""
concatenation:
        vertically  (row wise)
        horizontally (column wise)

        pd.concate([df1,df2],axis=0,ignore_index=true)
        [df1,df2]=
        axis=1

        ignore_index=true

"""
import pandas as pd
#vertically
df_region=pd.DataFrame({
    'customer id':[1,2],
    'name':['Gopal','Raju']
})

df_region2=pd.DataFrame({
    'customer id':[3,4],
    'name':['ram','manu']
})

df_concate=pd.concat([df_region,df_region2],ignore_index=True)
print(df_concate)
#horizontally
df_concate=pd.concat([df_region,df_region2],axis=1,ignore_index=True)
print(df_concate)