import sqlite3
import pandas as pd

conn = sqlite3.connect('CustomerBehavior.db')

df = pd.read_csv('CustomerBehavior.csv')
df.to_sql('customers', conn, if_exists='replace', index=False)

conn.commit()
conn.close()