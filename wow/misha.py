import pandas as pd

df = pd.read_csv("space.csv")

print(df['Status Mission'].value_counts())

import pandas as pd

#ГІПОТЕЗА: місце з найбільшою кількістю успішних місій знаходиться в Європі

# Групуємо дані за країною та статусом місії, підраховуємо кількість місій
places = df.groupby(['Location', 'Status Mission']).size().unstack(fill_value=0)

# Розраховуємо відсоткове співвідношення успішних та неуспішних місій
places['Success Rate'] = places['Success'] / (places['Success'] +places['Failure']) * 100
place = places['Success Rate'].idxmax()
print("Найкраще місце за відсотком успішних місій:", place)

