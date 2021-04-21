import sqlite3
import pandas as pd

#데이터 베이스 파일 연결
con = sqlite3.connect("employee.db")

cur = con.cursor()
cur.execute('SELECT * FROM employee')
rows = cur.fetchall()
cols = [column[0] for column in cur.description]

data_df = pd.DataFrame.from_records(data = rows, columns = cols)

con.close()
print(data_df)