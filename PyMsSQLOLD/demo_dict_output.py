import pymssql

conn = pymssql.connect(host='10.9.5.61\SQL', user='sa', password='adm123!!', database='dev_db_rajesh', as_dict=True)
cur = conn.cursor()

cur.execute('SELECT * FROM COMMON_env_details')

# for row in cur:
#     print(row)

ls = []
for row in cur:
    print(row)
    print(type(row))
    print(row['env'])

conn.close()