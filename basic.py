import sqlite3
import pandas as pd

# Load the CSV data into a DataFrame
df1 = pd.read_csv('basic_info.csv')

# Use the recommended method for filling missing values in specific columns
df1.fillna({'References': 'No reference'}, inplace=True)

# Connect to the SQLite database
conn = sqlite3.connect("db.sqlite3")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Remove all data from the existing table
cursor.execute("DELETE FROM basic_med_basic")

# Commit the transaction to apply the change
conn.commit()

# Insert the new data into the table
df1.to_sql('basic_med_basic', conn, if_exists='append', index=False, method='multi', chunksize=1000)

# Close the connection
conn.close()
