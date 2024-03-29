import psycopg2, regex

conn = psycopg2.connect( host="localhost", database="dspace", user="dspace", password="dspace")

cursor = conn.cursor()
cursor.execute("select m1.text_value, m2.text_value "\
               "from metadatavalue m1, metadatavalue m2, "\
               "collection2item coll, community2collection comm "\
               "where m1.metadata_field_id = 9 and m2.metadata_field_id = 70 "\
               "and m1.dspace_object_id = coll.item_id "\
               "and coll.collection_id = comm.collection_id "\
               "and comm.community_id = m2.dspace_object_id")

for row in cursor.fetchall():
    name, comm = row
    name = name.replace("|", ";")
    name = name.replace(":", ";")
    print(f"{name}|{comm}")

conn.close()
