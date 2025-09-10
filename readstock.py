import pandas as pd
import sqlite3
from datetime import datetime, timedelta

# read the csv file
df = pd.read_csv('data.csv', parse_dates=['ExpiryDate'])

# today's date
today = datetime.today().date()

# variable for expiration date gap
N = 30
cutoff = today + timedelta(days=N)

# expired items
expired = df[df['ExpiryDate'].dt.date <= today]

# expiring soon
expiring_soon = df[(df['ExpiryDate'].dt.date > today) & 
                   (df['ExpiryDate'].dt.date <= cutoff)]

# connect to SQLite (creates file if it doesn't exist)
conn = sqlite3.connect("pharmacy.db")

# save tables
expired.to_sql("expired_items", conn, if_exists="replace", index=False)
expiring_soon.to_sql("expiring_items", conn, if_exists="replace", index=False)

conn.close()

