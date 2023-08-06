"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="dasha888"
)

query = ("INSERT INTO customers VALUES ('ALFKI', 'Alfreds Futterkiste', 'Maria Anders'), ('AROUT', 'Around the Horn', 'Thomas Hardy'), ('BERGS', 'Berglunds snabbköp', 'Christina Berglund');"
         "INSERT INTO employees VALUES (1, 'Nancy', 'Davolio', 'Sales Representative', '1948-12-08', 'text'), (2, 'Andrew', 'Fuller', 'Vice President', '1952-02-19', 'text'), (3, 'Janet', 'Leverling', 'Inside Sales Coordinator', '1958-01-09', 'notes');"
         "INSERT INTO orders VALUES (10248, 'ALFKI', 1, '1996-07-04', 'Reims'), (10249, 'AROUT', 2, '1996-07-05', 'Münster'), (10250, 'BERGS', 3, '1996-07-08', 'Rio de Janeiro');"
         )

with conn:
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)