#VisualCounter

import pandas as pd
import matplotlib as plt

data = pd.read_csv('CodeCounterStorage.txt', sep = ' ', header=None)
data.head()
