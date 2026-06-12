#join=inner,outer,cross,left,right
#pd.merge(df1,df2,on="common column",how="type of join")
import pandas as pd

df1=pd.DataFrame({
    "Customer_ID":[1,2,3,4],
    "Name":["Priya","suresh","chintu","riya"]
})

df2=pd.DataFrame({
    "Customer_ID":[1,2,5,6],
    "Amount":[123,6655,87,9897]
})
#df_merged=pd.merge(df1,df2,on="Customer_ID",how="inner")
#df_merged=pd.merge(df1,df2,on="Customer_ID",how="outer")
#df_merged=pd.merge(df1,df2,on="Customer_ID",how="left")
df_merged=pd.merge(df1,df2,on="Customer_ID",how="right")
print(df_merged)