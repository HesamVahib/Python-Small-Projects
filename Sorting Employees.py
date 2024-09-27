import pymysql

cnx = pymysql.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="python",
)
cursor = cnx.cursor()

query = 'SELECT * FROM employees ORDER BY Height DESC, Weight;'
cursor.execute(query)

for (name, weight, height) in cursor:
    print(name, height, weight)

cnx.close()
