# -*- coding: utf-8 -*-
import MySQLdb
import csv
import datetime

#now = datetime.datetime.now() - datetime.timedelta(days=1)
#cutTime = now.strftime("%Y-%m-%d")

day_ex = 4
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="170270", db="sint_odessa", charset='utf8')
cursor = db.cursor()
#sql = "SELECT name,email,created_at FROM users WHERE created_at >= NOW()-INTERVAL %s DAY" %day_ex

sql = "SELECT users.id,1c_id,type_client_id,type_payment_id,client_name,delivery_town,delivery_street,delivery_house,delivery_house_block,delivery_office,phone,user_company,company_full,edrpou,inn,code_index,region,area,city,street,house,house_block,office,user_profiles.created_at,user_profiles.updated_at,name,email FROM user_profiles LEFT JOIN users ON user_profiles.user_id = users.id WHERE users.updated_at > NOW()-INTERVAL %s DAY OR user_profiles.updated_at > NOW()-INTERVAL %s DAY"
cursor.execute(sql,(day_ex,day_ex))
data = cursor.fetchall()

fp = open('/tmp/file.csv', 'w')
myFile = csv.writer(fp)
for rec in data:
    print rec[4]
    t = str(rec[2])
    myFile.writerows('t')
fp.close()

db.close()
#print cutTime