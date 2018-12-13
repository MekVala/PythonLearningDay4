# Test Fetching Data

import cx_Oracle

con = cx_Oracle.connect("ce140/ce140@192.168.29.152/xe")
cur = con.cursor()

cur.execute("select * from ADVERTISERS")

res = cur.fetchall()

for row in res:
    print(row)

con.close()