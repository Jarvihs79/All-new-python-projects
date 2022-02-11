import pandas as pd
df=pd.read_csv("sec_bhavdata_full_04022022.csv",skipinitialspace=True)
df.replace("-""",inplace=True)
df["CHANGE"]=df["CLOSE_PRICE"]-df["PREV_CLOSE"]
df["DELIV_PER"]=pd.to_numeric(df["DELIV_PER"])
data=df["SYMBOL"][("EQ" == df.SERIES) & (df.DELIV_PER >= 90) & (df["CHANGE"] > 0)]
ndf=pd.DataFrame(data)
ndf.to_csv("feb4anly.csv")
print(data)
