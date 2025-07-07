#import neccessary libraries
import sqlite3
import csv

#create and connect to a database
conn = sqlite3.connect('global_student_migration.db')
cursor = conn.cursor()

#create a table to store migration data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS
global_student_migration (
        origin_country TEXT,
        destination_country TEXT,
        course_name TEXT,
        enrollment_reason,
        year INTEGER
    )
''')

conn.commit()
print('Database and Table created successfully')

#read and parse the csv file
#with
file = open('global_student_migration.csv', newline='', encoding = 'utf-8')
reader = csv.DictReader(file)
rows_inserted = 0
    
for row in reader:
    origin = row['origin_country']
    destination = row['destination_country']
    course = row['course_name']
    reason = row['enrollment_reason']
    year = int(row['year_of_enrollment']) if row['year_of_enrollment'].isdigit() else None
    
    cursor.execute('''
            INSERT INTO
    global_student_migration(origin_country, destination_country, course_name, enrollment_reason, year) VALUES (?, ?, ?, ?, ?)
            ''', (origin, destination, course, reason, year))
    rows_inserted += 1
    
conn.commit()
    
print('Inserted {row_inserted} rows into database.')
conn.close()


