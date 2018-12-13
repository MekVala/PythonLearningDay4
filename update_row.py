# Update Query Test

import cx_Oracle
import datetime

now = datetime.datetime.now()

try:
    con = cx_Oracle.connect("ce140/ce140@192.168.29.152/xe")
    cur = con.cursor()

    cur.execute("""update ADVERTISERS set REGISTRY_DATE='%s'
    where ADVERTISER_ID=1""" %now.strftime("%d-%b-%y"))

    print("Row Updated")

    con.commit()
    con.close()

except Exception as e:
    print("Error Connecting Database: %s" % str(e))

