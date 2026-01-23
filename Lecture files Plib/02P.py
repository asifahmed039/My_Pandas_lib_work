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
df=pd.read_json("Lecture files Plib\sample_Data.json")
print(df)
