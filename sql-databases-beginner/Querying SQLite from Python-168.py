## 3. Connecting to the Database ##

import sqlite3

conn = sqlite3.connect("jobs.db")

## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

qry = "select Major from recent_grads;"
cursor.execute(qry)
majors = cursor.fetchall()
print(majors[0:3])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

qry = "select Major, Major_category from recent_grads;"
cursor.execute(qry)
five_results = cursor.fetchmany(5)


## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3
conn = sqlite3.connect("jobs2.db")
cursor = conn.cursor()
qry = "select Major from recent_grads order by Major Desc;"
cursor.execute(qry)
reverse_alphabetical = cursor.fetchall()

conn.close()