#interpolate()--givres the estimated value in the data. 
'''for ex-
10
20

40
50
it will give 30 on the missing value place

Syntax=df.interpolate(method="linear",axis=0(row),inplace=True)
method=linear,polynomial,time
usage-
1-time series data
2-numeric data with trends
3-avoid droping rows
'''
import pandas as pd
data={
    "time":[1,2,3,4,5],
    "value":[10,None,30,40,None]
}
df=pd.DataFrame(data)
#df.interpolate(model="linear",axis=1,inplace=True)
df.interpolate(inplace=True)
print(df)