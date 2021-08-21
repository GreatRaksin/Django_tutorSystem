import sqlite3, csv

# con = sqlite3.connect(":memory:")
con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

with open('output.csv', 'r') as table:
    dr = csv.DictReader(table)  # comma is default delimiter
    to_db = [(i['\ufeffid'], i['l_name'], i['f_name'], i['fath_name'], i['img_link'], i['anchor'], i['school'], i['city_id'], i['subject_id']) for i in dr]

cur.executemany("INSERT INTO tutors_tutor VALUES (?,?,?,?,?,?,?,?,?);", to_db)
con.commit()