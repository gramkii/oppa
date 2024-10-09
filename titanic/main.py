import pandas as pd

df = pd.read_csv("titanic.csv")

print(df.groupby('Sex')['Survived'].mean())


table = df.pivot_table(index='Survived', columns='Pclass', values = 'Age', aggfunc = 'mean')
print(table)

df.info()

df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1 ,inplace=True)
df.info()

df['Embarked'].fillna('S', inplace=True)
df.info()

age1 = df[df['Pclass'] == 1]['Age'].mean() 
age2 = df[df['Pclass'] == 2]['Age'].mean() 
age3 = df[df['Pclass'] == 3]['Age'].mean() 

def fillAge(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age1
        if row['Pclass'] == 2:
            return age2
        if row['Pclass'] == 3:
            return age3
    return row['Age']

df['Age'] = df.apply(fillAge, axis = 1 )
df.info()
