import pandas as pd
column = ['target','id','date','flag','user','text']

df = pd.read_csv('tweets.csv', encoding='latin1',names=column)

df['sentiment'] = df['target'].map({0:'negative',2:'neutral',4:'positve'})

#print(df)
# print(df.columns)
# print(df['sentiment'])

df_new = df[['text','target','sentiment']]
print(df_new)

#data_Cleaning Task
#1: convert_to Lower Case
#2: Remove URLS using apply, lambda and regex
#3:remove mentions
#4: remove hastags
