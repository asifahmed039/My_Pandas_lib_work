import pandas as pd
#read the data from csv file into a dataframe
"""
    encoding  latin  or utf-8
    for cloud data
        gcsfs 
    """
     #read file 
# df=pd.read_csv("Lecture files Plib\sales_data_sample.csv",encoding="latin1")
# df=pd.read_excel("Lecture files Plib\SampleSuperstore.xlsx")
# df=pd.read_json("Lecture files Plib\sample_Data.json")
df1=pd.read_excel("My_Pandas_Work\Lecture files Plib\SampleSuperstore.xlsx")
print(df1)
