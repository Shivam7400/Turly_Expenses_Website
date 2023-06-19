import psycopg2

conn = psycopg2.connect(database="incomeexpensesdb",
                        host="127.0.0.1",
                        user="postgres",
                        password="new_password",
                        port="5432")
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS your_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER
)
'''
cursor.execute(create_table_query)
conn.commit()

insert_data_query = '''
INSERT INTO your_table (name, age)
VALUES (%s, %s)
'''
data = ("John", 30)
cursor.execute(insert_data_query, data)
conn.commit()

select_data_query = '''
SELECT * FROM your_table
'''
cursor.execute(select_data_query)
records = cursor.fetchall()
for row in records:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])
select_data_query = '''
SELECT * FROM your_table
'''
cursor.execute(select_data_query)
records = cursor.fetchall()
for row in records:
    print("ID:", row[0])
    print("Name:", row[1])
    print("Age:", row[2])


cursor.close()
conn.close()
