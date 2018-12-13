# Test delete row
import cx_Oracle

con = cx_Oracle.connect("ce140/ce140@192.168.29.152/xe")

cur = con.cursor()

cur.execute("delete ADVERTISERS where ADVERTISER_ID=1")
print("Row Deleted")
con.commit()

con.close()