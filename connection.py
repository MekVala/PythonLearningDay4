# Initial Connection Test
import cx_Oracle

con = cx_Oracle.connect("ce140/ce140@192.168.29.152/xe")

print("Connected to version %s" %con.version)

con.close()