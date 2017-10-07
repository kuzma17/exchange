import MySQLdb
import csv

day_ex = 15
file_csv = '/tmp/file.csv'
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="170270", db="sint_odessa", charset='utf8', use_unicode=False)
cursor = db.cursor()

sql = "SELECT users.id,1c_id,type_client_id,type_payment_id,client_name,delivery_town,delivery_street,delivery_house,delivery_house_block,delivery_office,phone,user_company,company_full,edrpou,inn,code_index,region,area,city,street,house,house_block,office,user_profiles.created_at,user_profiles.updated_at,name,email FROM user_profiles LEFT JOIN users ON user_profiles.user_id = users.id WHERE users.updated_at > NOW()-INTERVAL %s DAY OR user_profiles.updated_at > NOW()-INTERVAL %s DAY"
cursor.execute(sql, (day_ex, day_ex))
#data = cursor.fetchall()
db.close()

fp = open(file_csv, 'w')
myFile = csv.writer(fp, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
myFile.writerows(cursor)
fp.close()


