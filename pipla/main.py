import pandas as pd

df = pd.read_csv("GooglePlayStore_wild.csv")

information = df.info()
print(information)

lenght = len(df[pd.isnull(df['Rating'])])
print(lenght)


df['Rating'].fillna(10, inplace=True)
information = df.info()
print(information)


print(df['Size'].value_counts())

def peremoga(size):
    if size[-1] == "M":
        return float(size[:-1])
    elif size[-1] == 'k':
        return float(size[:-1])/1024
    return -1

df['Size'] = df['Size'].apply(peremoga)    

print(df['Size'].value_counts())


def stovp(date):
    month = date.split()[0]
    seasons = {
        'Winter': ['December', 'January', 'February'],
        'Spring': ['March', 'April', 'May'],  
        'Summer': ['June', 'July', 'August'],
        'Autumn': ['September', 'October', 'November'],        
    }
    for season in seasons:
        if month in seasons[season]:
            return season
    return "No data"

df['Season'] = df['Last Updated'].apply(stovp)

print(df['Season'].value_counts())

import matplotlib.pyplot as pl

#df['Size'].plot(kind='hist')
#pl.show()

df['Season'].value_counts().plot(kind= 'pie')
pl.show()