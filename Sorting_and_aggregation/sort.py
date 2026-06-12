import pandas as pd
data={
    "Name":["Priyanka","Shruti","Ayush","Himanshu","Tripti","Angel"],
    "age":[32,21,28,20,18,19],
    "Salary(in USD)":[20,76,23,54,32,45]
}
df=pd.DataFrame(data)
#df.sort_values(by="age",ascending=False,inplace=True)
df.sort_values(by=["age","Salary(in USD)"],ascending=[False,True],inplace=True)
print(df)