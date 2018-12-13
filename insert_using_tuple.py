# Insert Multiple Using Tuple

import cx_Oracle

print("Connecting Database")
con = cx_Oracle.connect("ce140/ce140@192.168.29.152/xe")
print("Database Connected !")
cur = con.cursor()

rows = [(2, 'Denvour Outdoors', 'McMen', 'John', '891-342-4170', 'Las Vegas', 'NV', 'USA', '12-JUN-2002'),
        (3, 'Ford Outdoors', 'Andrew', 'Harry', '321-341-0789', 'NewYork', 'NY', 'USA', '11-NOV-2000')]

cur.bindarraysize = len(rows)

print("Inserting Row !")
cur.executemany("insert into ADVERTISERS(ADVERTISER_ID,ADVERTISER_NAME,CONTACT_LNAME,CONTACT_FNAME,PHONE_NUMBER,CITY,"
                "ST,COUNTRY,REGISTRY_DATE) values(:1,:2,:3,:4,:5,:6,:7,:8,:9)", rows)
print("Row Inserted !")

con.commit()
con.close()
