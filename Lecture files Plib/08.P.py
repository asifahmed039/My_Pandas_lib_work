""""
    1-Select specific column
    2-Filter rows
    3-Combine multiple conditions

    1-Square brackets
    2-Boolean condition

    Selecting columns
    1-a series
    2-dataframe multiple columns of data

    column=df["column_name"]
    subset=df["column1","column2".....]

    Filtering rows
    boolean indexing

    #based on a single conditoin
    filtered_row=df[df["salary"]>50000]

    #combine multiple condition
    filtered_rows=df[df["salary"]>50000 & (df["col2]<80000)]


"""
import pandas as pd

data={
    "name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print("names(singlec col return series")
#Select single column
Name=df["name"]
print(Name)
# print(df["name"])

#print multiple columns
subset=df[['name','Salary','Age']]
print(subset)

