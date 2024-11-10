import sqlite3
import pandas as pd

df1 = pd.read_csv('phyto.csv')
df1['LogP'] = df1['LogP'].fillna(0)  # Fill missing LogP values with 0

conn = sqlite3.connect("db.sqlite3")
df1.to_sql('phytochem_med_phytochem', conn, if_exists='append', index=False, method='multi', chunksize=1000)
conn.close()
