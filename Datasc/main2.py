import pandas as pd
df = pd.read_csv("GoogleApps.csv")

data = df['Category'].value_counts() #value_counts - кількість значень
print(data)



data2 = data = df['Content Rating'].value_counts()
print(data2)
result = round(data2['Teen'] / data2['Everyone 10+'], 2)
print(result)



data3 = data = df['Rating'].value_counts()
print(data3)
dod = df[df['Type'] == 'Paid']['Rating'].mean()
print(dod)


dod2 = df[df['Type'] == 'Free']['Rating'].mean()
print(dod2)


print(round(dod-dod2, 2))




dodatok = df[df['Category'] == 'COMICS']['Size'].min()
print(dodatok)

dodatok = df[df['Category'] == 'COMICS']['Size'].max()
print(dodatok)
