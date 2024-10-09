import pandas as pd

pd.set_option('display.max_rows', None)
df = pd.read_csv("Space.csv")

print(df.info())
 
df['Rocket'].fillna(-1, inplace=True)

a = df['Status Mission'].value_counts()
print(a)

def Country(company):
    state = company.split()[-1]
    return state

df['Company Name'] = df['Location'].apply(Country)

countries = df['Company Name'].value_counts()
print(countries)

#success = df.groupby(by='Company Name')['Status Mission'].value_counts()
#print(success)

successq = df.groupby(by='Company Name')['Datum'].value_counts()
print(successq)