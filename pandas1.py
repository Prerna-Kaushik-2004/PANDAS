import pandas as pd
data={
    "Name":["Priyanka","Shruti","Ayush","Himanshu","Tripti","Angel"],
    "age":[20,21,24,27,28,29],
    "Salary(in USD)":[20,40,23,54,32,45]
}
df=pd.DataFrame(data)
print(df)
print("*"*50)
#df.to_csv("Employee.csv",index=False)
#print(df.info())
#print(df.describe())
#print(df.shape)
#print(df.columns)
#Query
print(df[(df["Salary(in USD)"]>32) &(df["age"]>23) ])
