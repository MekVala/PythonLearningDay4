# procedure call test
import cx_Oracle

con = cx_Oracle.connect("ce140/ce140@192.168.29.152/xe")

cur = con.cursor()
py_inOut = cur.var(cx_Oracle.STRING)
py_inOut.setvalue(0, 'Value')
cur.callproc('proc_inOut', [py_inOut])

print("Output: ", py_inOut.getvalue())
con.close()
