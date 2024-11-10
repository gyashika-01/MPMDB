import sqlite3
import pandas as pd

# Load the CSV data into a DataFrame
df1 = pd.read_csv('trans.csv')

# Handle missing values in the 'NCBI_link' column
df1['NCBI_link'] = df1['NCBI_link'].fillna('N/A')  # Replaces missing values with 'N/A'

# Connect to the SQLite database
conn = sqlite3.connect("db.sqlite3")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Remove all data from the existing table
cursor.execute("DELETE FROM transcriptom_med_transcriptom")

# Commit the transaction to apply the change
conn.commit()

# Insert the new data into the table
df1.to_sql('transcriptom_med_transcriptom', conn, if_exists='append', index=False, method='multi', chunksize=1000)

# Close the connection
conn.close()
