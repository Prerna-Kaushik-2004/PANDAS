#groupby--is used to group the data and perform aggregation
import pandas as pd
data={
    "Name":["Priyanka","Shruti","Ayush","Himanshu","Tripti","Angel"],
    "age":[32,21,28,32,28,19],
    "Salary(in USD)":[20,76,23,54,32,45]
}
df=pd.DataFrame(data)
#grp=df.groupby("age")["Salary(in USD)"].sum()
grp=df.groupby(["age","Name"])["Salary(in USD)"].sum()
print(grp)
