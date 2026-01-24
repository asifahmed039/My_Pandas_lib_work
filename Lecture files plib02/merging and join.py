 #Merging and joins
"""
 syntax:
    pd.merge(df1,df2,on="col_name",how='types of join')

"""
import pandas as pd

df_customer=pd.DataFrame({
    "customer_id":[1,2,3],
    "name":['Ramesh','Suresh','Kalpesh']
})

df_orders=pd.DataFrame(
    {
      "customer_id":[1,2,4],
      'orderAmount':[250,450,350]  
    }
)
                                                            #join
df_merge=pd.merge(df_customer,df_orders,on='customer_id',how="inner")
print(df_merge)

"""
joins:
    outer  inner  left   right

    cross join
        idf=m rows
        2df=n rows
        m*n rows
"""

