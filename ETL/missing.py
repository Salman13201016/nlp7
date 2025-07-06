import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Name': ['Salman', 'Rina', 'Tariq', np.nan, 'Nila'],
    'Age': [25, np.nan, 22, 28, 24],
    'City': ['Dhaka', 'Chittagong', np.nan, 'Khulna', 'Rajshahi']
}

df = pd.DataFrame(data)

print(df.head())

#how to handle missing data
#detec missing
print(df.isnull().sum())

# df_drop = df.dropna(how='all')

# #Task= Remove Column
# #task = x% null thakle

# print(df_drop)

#fill Missing Values
#-Constant value

df_cons = df.fillna('unknown')

# df['Age'].fillna(df['Age'].mean(),inplace=True)
# print(df)

df_fill = df.fillna(method='ffill')

df_bfill = df.fillna(method='bfill')
print(df_bfill,df_fill)

#avg_forward_fill
#avg_backward_fill
#interpolation: Linear vs Polygon