# courser attributes

import cx_Oracle

con = cx_Oracle.connect("ce140/ce140@192.168.29.152/xe")
cur = con.cursor()

cur.execute("select * from ADVERTISERS")

print("Columns:")
for col in cur.description:
    print(col[0])
print("Total Row Fetched:", cur.rowcount)
