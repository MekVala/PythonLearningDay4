# creating table and insert a row
import cx_Oracle

con = cx_Oracle.connect("ce140/ce140@192.168.29.152/xe")

cur = con.cursor()
# cur.execute("""CREATE TABLE "ADVERTISERS" ( "ADVERTISER_ID" NUMBER(10,0), "ADVERTISER_NAME" VARCHAR2(20 BYTE),
# "CONTACT_LNAME" VARCHAR2(20 BYTE), "CONTACT_FNAME" VARCHAR2(20 BYTE),"PHONE_NUMBER" VARCHAR2(20 BYTE),
# "CITY" VARCHAR2(10 BYTE),"ST" CHAR(2 BYTE),"COUNTRY" CHAR(20 BYTE),"REGISTRY_DATE" DATE)""")
#
# print("Table Created !")

cur.execute("""Insert into ADVERTISERS
(ADVERTISER_ID,ADVERTISER_NAME,CONTACT_LNAME,CONTACT_FNAME,PHONE_NUMBER,CITY,ST,COUNTRY) 
values (1,'ROLEY COMPANIES','SMITH','ERIC','713-882-0456','HOUSTON','TX','India')""")

print("Row Inserted !")
con.commit()

con.close()

