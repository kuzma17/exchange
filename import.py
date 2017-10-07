import MySQLdb
import csv

day_ex = 15
file_csv = '/tmp/file.csv'

field_user = ("name,email,created_at,updated_at")
field_user_profije = ("id","1c_id","type_client_id","type_payment_id","client_name","delivery_town","delivery_street","delivery_house","delivery_house_block","delivery_office","phone","user_company","company_full","edrpou","inn","code_index","region","area","city","street","house","house_block","office","created_at","updated_at")
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="170270", db="sint_odessa", charset='utf8', use_unicode=False)
cursor = db.cursor()

csv_data = csv.reader(file(file_csv), delimiter=';')

for row in csv_data:
    if row[0] != '' :
        print 'update'
        i = 0
        sql = 'UPDATE user_profiles SET '
        while i <= 24:
            sql += field_user_profije[i] + ' = "' + row[i] + '"'
            if i != 24:
                sql += ', '
            i = i + 1

        sql += ' WHERE user_id = ' + row[0]
        print sql
        cursor.execute(sql)
    else:
        print 'insert'


db.close()



