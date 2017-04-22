## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect("dbname = dq user = dq")
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname = dq user = dq")
cur = conn.cursor()

qry = """
create table notes 
(
    id integer primary key, 
    body text, 
    title text
)
"""
cur.execute(qry)
conn.close()

## 5. SQL Transactions ##

import psycopg2
conn = psycopg2.connect("dbname = dq user = dq")
cur = conn.cursor()

qry = """
create table notes 
(
    id integer primary key, 
    body text, 
    title text
)
"""
cur.execute(qry)
conn.commit()
conn.close()

## 6. Autocommitting ##

conn = psycopg2.connect("dbname = dq user = dq")
conn.autocommit = True
cur = conn.cursor()
qry = """
create table facts
(
    id integer primary key, 
    country text, 
    value integer
)
"""
cur.execute(qry)
conn.close()

## 7. Executing queries ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');")
cur.execute("SELECT * from notes;")
rows = cur.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
qry = "CREATE DATABASE income OWNER dq"
cur.execute(qry)

conn.close()


## 9. Deleting a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
qry = "drop database income"
cur.execute(qry)

conn.close()