import pandas as pd

df = pd.read_csv("GoogleApps.csv")

#print(df.head())

#print(df.tail())

#print(df.info())

#print(df.describe())

dodatok = df[df['Type'] == 'Paid']['Price'].min()
print(dodatok)



dodatok = df[df['Type'] == 'Paid']['Reviews'].max()
print(dodatok)

dodatok = df[df['Type'] == 'Free']['Reviews'].max()
print(dodatok)