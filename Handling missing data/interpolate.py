import pandas as pd
data={
    "time":[1,2,3,4,5],
    "value":[10,None,30,40,None]
}
df=pd.DataFrame(data)
#df.interpolate(model="linear",axis=1,inplace=True)
df.interpolate(inplace=True)
print(df)