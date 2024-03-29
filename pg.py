import psycopg2

conn = psycopg2.connect( host="localhost", database="dspace", user="dspace", password="dspace")

cursor = conn.cursor()
cursor.execute("select m.text_value from metadatavalue m, collection c where m.dspace_object_id = c.uuid")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
