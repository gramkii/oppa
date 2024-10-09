import pandas as pd
import matplotlib.pyplot as pl
df = pd.read_csv("GooglePlayStore_wild.csv")


data_for_the_Graphic_ = pd.Series(data = [12, 43, 15, 5, 7],
                                  index = [1,2,3,4,5])

data_for_the_Graphic_.plot()
pl.show()