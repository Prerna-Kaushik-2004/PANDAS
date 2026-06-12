#pd.concat(df1,df2,axis=0(row)/1(column),ignore_index=True)
#vertically=row
#horizontally=column
import pandas as pd
#region1
df1=pd.DataFrame({
    "Customer_ID":[1,2],
    "Name":["Rohel","Shubham"]
})
#region2
df2=pd.DataFrame({
    "Customer_ID":[3,4],
    "Name":["shohel","Shubhi"]
})
#concatenate vertically
df_concat=pd.concat([df1,df2],ignore_index=True)
print(df_concat)
#concatenate horizontally
df_concat=pd.concat([df1,df2],axis=1,ignore_index=True)
print(df_concat)