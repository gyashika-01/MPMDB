import sqlite3
import pandas as pd

# Load the CSV data into a DataFrame
df1 = pd.read_csv('proteome.csv')

# Connect to the SQLite database
conn = sqlite3.connect("db.sqlite3")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Remove all data from the existing table
cursor.execute("DELETE FROM proteom_med_proteom")

# Commit the transaction to apply the change
conn.commit()


# Insert the new data into the table
df1.to_sql('proteom_med_proteom', conn, if_exists='append', index=False, method='multi', chunksize=1000)

# Close the connection
conn.close()
