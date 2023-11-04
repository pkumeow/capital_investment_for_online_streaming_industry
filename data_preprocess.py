import pandas as pd
df = pd.read_csv('TVdata_original.csv')
df.to_csv('TVdata_original_col.csv')
df['playable_date'] = pd.to_datetime(df['playable_date'])
df['time']=(df['playable_date'].dt.year-2020)*12+df['playable_date'].dt.month

min_fans = min(min(df['actor1_fans']),min(df['actor2_fans']))
df['actor1_fans'].fillna(min_fans, inplace=True)
df['actor2_fans'].fillna(min_fans, inplace=True)
df['actor_top2_fans']=df['actor1_fans']+df['actor2_fans']

df['platform_cnt_AYTM'] = df['platform_A']+df['platform_Y']+df['platform_T']+df['platform_M']

df['theme_guzhuang']=df['theme'].apply(lambda x:1 if'古装' in str(x) else 0)

df[['brand_cnt', 'director_top20', 'writer_top20', 'time', 'actor_top2_fans', 'platform_cnt_AYTM', 'theme_guzhuang']].to_csv('TVdata_processed_col.csv')