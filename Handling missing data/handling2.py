#fillna(value,inplace=True)
import pandas as pd
data={
    "Name":["Priyanka","Shruti",None,"Himanshu","Tripti","Angel"],
    "age":[20,21,24,27,None,29],
    "Salary(in USD)":[20,40,23,54,None,45]
    }
df=pd.DataFrame(data)
#df.fillna(0,inplace=True)  
df["age"].fillna(df["age"].mean(),inplace=True)
print(df) 