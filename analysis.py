#Import neccessary libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#Connect to the database
conn = sqlite3.connect('global_student_migration.db')

#Query for Top 10 destination countries
query_1 = '''
    SELECT destination_country, COUNT(*) as student_count
    FROM global_student_migration
    GROUP BY destination_country
    ORDER BY student_count DESC
    LIMIT 10
'''

#Read into a pandas
df = pd.read_sql_query(query_1, conn)

print(df)

#Query for top 10 origin countries
query_2 = '''
    SELECT origin_country, COUNT(*) as student_count
    FROM global_student_migration
    GROUP BY origin_country
    ORDER BY student_count DESC
    LIMIT 10
'''

#Read into pandas
of = pd.read_sql_query(query_2, conn)

print(of)

#Query for Top 10 courses being studied
query_3 = '''
    SELECT course_name, COUNT(*) as student_count
    FROM global_student_migration
    GROUP BY course_name
    ORDER BY student_count DESC
    LIMIT 10
'''

#Read into pandas
cf = pd.read_sql_query(query_3, conn)

print(cf)

#Query for Top 5 reason for going abroad
query_4 = '''
    SELECT enrollment_reason, COUNT(*) as student_count
    FROM global_student_migration
    GROUP BY enrollment_reason
    ORDER BY student_count DESC
    LIMIT 5
'''

#Read into pandas
ef = pd.read_sql_query(query_4, conn)

print(ef)

# Query: count students by year
query_5 = '''
    SELECT year, COUNT(*) as student_count
    FROM global_student_migration
    WHERE year IS NOT NULL
    GROUP BY year
    ORDER BY year
'''

# Get DataFrame
yf = pd.read_sql_query(query_5, conn)

print(yf)

conn.close()

#Plotting
plt.figure(figsize=(12, 6))
plt.barh(df['destination_country'], df['student_count'], color='skyblue')
plt.xlabel('Number of Students')
plt.title('Top 10 Destination Countries for Global Student Migration')
plt.gca().invert_yaxis()  # Highest bar on top
plt.show()

#Plotting
plt.figure(figsize=(12, 6))
plt.barh(of['origin_country'], of['student_count'], color='red')
plt.xlabel('Number of Students')
plt.title('Top 10 Countries of Origin for Global Student Migration')
plt.gca().invert_yaxis()  # Highest bar on top
plt.show()

#Plotting
plt.figure(figsize=(12, 6))
plt.barh(cf['course_name'], cf['student_count'], color='purple')
plt.xlabel('Number of Students')
plt.title('Top 10 Courses of Enrollment for Global Student Migration')
plt.gca().invert_yaxis()  # Highest bar on top
plt.show()

#Plotting
plt.figure(figsize=(12, 6))
plt.barh(ef['enrollment_reason'], ef['student_count'], color='green')
plt.xlabel('Number of Students')
plt.title('Top 5 reasons of enrollment for Global Student Migration')
plt.gca().invert_yaxis()  # Highest bar on top
plt.show()

#Plotting trend line
plt.figure(figsize=(10, 6))
plt.plot(yf['year'], yf['student_count'], marker='o', linestyle='-', color='teal')
plt.xlabel('Year')
plt.ylabel('Number of Students')
plt.title('Global Student Migration Trend Over Years')
plt.xticks(yf['year'], rotation=45)
plt.grid(True)
plt.show()
