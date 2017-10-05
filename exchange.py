import MySQLdb
import datetime

now = datetime.datetime.now() - datetime.timedelta(days=5)
cutTime = now.strftime("%Y-%m-%d")

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="170270", db="sint_odessa", charset='utf8')
cursor = db.cursor()
sql = "SELECT name,email FROM users WHERE created_at >= "+ cutTime
cursor.execute(sql)
data = cursor.fetchall()

for rec in data:
    print rec[0] +' '+ rec[1]

db.close()

print cutTime