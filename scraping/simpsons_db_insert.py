from __future__ import print_function
import csv
import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="pma",  # your username
                     passwd="admin",  # your password
                     db="acma_cartoon")  # name of the data base

with open('./simpsons_original_files/simpsons_script_lines.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    columns = next(reader)
    query = 'insert into simpsons_script_lines({0}) values ({1})'
    query = query.format(','.join(columns), ','.join(['%s' for i in range(len(columns))]))
    cursor = db.cursor()
    for data in reader:
        for i in range(len(data)):
            if data[i] == '':
                data[i] = 'NULL'
        if len(data) == 13:
            cursor.execute(query, data)
        else:
            print(data)

    db.commit()

db.close()