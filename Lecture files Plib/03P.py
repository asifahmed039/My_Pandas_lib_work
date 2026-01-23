import pandas as pd


data={
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[10,20,30],
    "City":['Nagpur','Mumbai','Delhi']
}
#converting data into file.
df=pd.DataFrame(data)
print(df)
#save into csv file
# df.to_csv("output.csv")
df.to_json("second.json",index=False)
print(df)

# df.to_excel("output.xlsx",index=False)
print(df.info())