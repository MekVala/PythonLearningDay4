# Update Query Test

import cx_Oracle
try:
    con = cx_Oracle.connect("ce140/ce140@192.168.29.152/xe")
    cur = con.cursor()

    cur.execute("""update ADVERTISERS set REGISTRY_DATE=sysdate
    where ADVERTISER_ID=1""")

    print("Row Updated")

    con.commit()
    con.close()

except Exception as e:
    print("Error Connecting Database: %s" % str(e))

