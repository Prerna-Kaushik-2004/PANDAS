#aggregate=mean(),sum(),min(),max()
import pandas as pd
data={
    "Name":["Priyanka","Shruti","Ayush","Himanshu","Tripti","Angel"],
    "age":[32,21,28,20,18,19],
    "Salary(in USD)":[20,76,23,54,32,45]
    }
df=pd.DataFrame(data)
avg_salary=df["Salary(in USD)"].mean()
print(avg_salary)