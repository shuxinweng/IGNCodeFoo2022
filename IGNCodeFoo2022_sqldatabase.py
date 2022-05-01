import pandas as pd
import pypyodbc as odbc

"""
Reading CSV file using pandas
"""

df = pd.read_csv('codefoobackend_cfgames.csv')

"""
Sanitizing data (Removing "bad" data with no long_description (assuming data not completed), 11 removed.)
"""

df.drop(df.query('long_description.isnull()').index, inplace = True)

"""
Normalizing data (Removing columns with data redundancy. Removed id because clients doesn't need to know the id of the data.
                    Removed short_name because short_names are mostly the same as name and some data does not have a short_name.
                    Removed short_description because long_description has a more detailed description and it is redundant.
                    Removed slug because it is mostly just the same the name.
                    Changed any date time values to the date time value that sql database can understand using the to_datetime in pandas.)
"""

df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%Y-%m-%d %H:%M:%S')
df['updated_at'] = pd.to_datetime(df['updated_at']).dt.strftime('%Y-%m-%d %H:%M:%S')

columns = ['media_type', 'name', 'long_description', 'created_at', 'updated_at', 'review_url', 'review_score',
            'genres', 'created_by', 'published_by', 'franchises', 'regions']

df_data = df[columns]
records = df_data.values.tolist()

"""
Indexing data (I wanted to rearrange the review_score column so that it will be rearranged into largest to smallest values
                this can help the client to access to the highest ratings faster.)
"""

"""
Create SQL Serve Connection String
"""

DRIVER = "SQL Server"
SERVER_NAME = "SHU"
DATABASE_NAME = "IGNCodeFoo"

def connection_string(driver, server_name, database_name):
    conn_string = f'''
        DRIVER={{{driver}}};
        SERVER={server_name};
        DATABASE={database_name};
        Trust_Connection=yes;
    '''
    return conn_string

"""
Create database connection instance
"""

try:
    conn = odbc.connect(connection_string(DRIVER, SERVER_NAME, DATABASE_NAME))
except odbc.DatabaseError as e:
    print('Data Error:')
    print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error:')
    print(str(e.value[1]))

"""
Create a cursor connection
"""

sql_insert = """
    INSERT INTO IGNCodeFooData
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

try:
    cursor = conn.cursor()
    cursor.executemany(sql_insert, records)
    cursor.commit();
except Exception as e:
    cursor.rollback()
    print(str(e[1]))
finally:
    print('Task is complete.')
    cursor.close()
    conn.close()

