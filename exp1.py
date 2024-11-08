import pandas as pd
import numpy as np
series_A=pd.Series([10,20,30,40,50])
series_B=pd.Series([40,50,60,70,80])
union=pd.Series(np.union1d(series_A,series_B))
intersect=pd.Series(np.intersect1d(series_A,series_B))
notcommonseries=union[-union.isin (intersect)]
print(notcommonseries)
print('largest number in series_A is:',series_A.max())
print('smallest number in series_A is:',series_A.min())
print('the sum of series_B is:',series_B.sum())
print('the average of series_A is:',series_A.mean())
print('the median of series_B is:',series_B.median())
