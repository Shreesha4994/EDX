import pandas as pd 

df=pd.read_csv("qw.csv")

print(df)

import matplotlib.pyplot as plt
plt.plot(df['Instruction Score'],'ro')
plt.show()
