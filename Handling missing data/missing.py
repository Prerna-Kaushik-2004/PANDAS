#NaN-Not a number
#None-for object type datatype

import pandas as pd
data={
    "Name":["Priyanka","Shruti",None,"Himanshu","Tripti","Angel"],
    "age":[20,21,24,27,None,29],
    "Salary(in USD)":[20,40,23,54,None,45]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())