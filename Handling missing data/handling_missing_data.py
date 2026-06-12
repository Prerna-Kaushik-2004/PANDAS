#dropna(axix=0/1,inplace=True)
#axis=0---for row
#axis=1----for column
import pandas as pd
data={
    "Name":["Priyanka","Shruti",None,"Himanshu","Tripti","Angel"],
    "age":[20,21,24,27,None,29],
    "Salary(in USD)":[20,40,23,54,None,45]
    }
df=pd.DataFrame(data)
df.dropna(inplace=True)
print(df)