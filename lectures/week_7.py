import pandas as pd

df = pd.DataFrame(
    {
        "col1":range(10),
        "col2":range(10,20)
    },
    index = list("acgfhibdje")
)

print(df)

ser = df.loc[["b","c","d","e"],"col1"]
print(ser)

df1 = df.loc[["b","d","f","j"],["col1"]]
print(df1)
print(type(df1))


df2 = pd.DataFrame(
    {"col1":range(0,20),
     "col2":range(20,40),
    "col3":range(40,60)
    }
)
print(df2)

# row1 = list(range(0,len(df2.index),2))
# a = [i for i in range(0,20,2)]


even_list=[]
for i in range(0,20,2):
    even_list.append(i)

print(even_list)
df3 = df2.iloc[even_list,[1]]
print(df3)