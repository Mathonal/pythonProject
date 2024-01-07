import sqlite3
from sqlite3 import Connection
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).parent
def create_sqlite_connection(db_path:Path)->Connection:
    connection = None
    try:
        connection = sqlite3.connect(str(db_path))
        print("Database connection successful")
    except Exception as err:
        print(f"Error: '{err}'")

    return connection

# # fetchone as iteror on cursor itself
# cursor.execute("""SELECT name, age FROM users""")
# user1 = cursor.fetchone()
# print(user1)
#
# # Get count
# count = cursor.rowcount
#
# # Fetchall as an iteration creator
# cursor.execute("""SELECT id, name, age FROM users""")
# rows = cursor.fetchall()
# for row in rows:
#     print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
#
# # Modify entry
# cursor.execute("""UPDATE users SET age = ? WHERE id = 2""", (31,))
#
# # Rollback -> nullify last entries up to last commit (executes)
# conn.rollback() # only the update in this case
#
# # Delete
# cursor = conn.cursor()
# cursor.execute("""
# DROP TABLE users
# """)
# conn.commit()
#
# # Disconnect
# conn.close()

if __name__ =="__main__":
    db_path = PROJECT_DIR / "my_db.sqlite"
    csv_path = PROJECT_DIR / "train_ex.csv"
    conn = create_sqlite_connection(db_path)
    tbl = pd.read_csv(csv_path)

    tbl.to_sql("building", conn, if_exists='replace', index=False)

    tbl_read = pd.read_sql_query('SELECT * FROM building', conn)
    print(tbl_read.dtypes)

    cursor = conn.cursor()

    # fetchone as iteror on cursor itself
    cursor.execute("""SELECT load, temperature FROM building""")
    count = cursor.rowcount
    line1 = cursor.fetchone()
    print(line1)

    pass