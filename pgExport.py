import psycopg2
import os
import datetime

# connecting to pg server
connect_pg = psycopg2.connect(
    user="postgres", 
    password="2208711Sel", 
    host="127.0.0.1",
    port = "5432", 
    database = "truckgenie-dev"
    )
cur = connect_pg.cursor()

#Exports as csv with timestamp to a directory
def pg_export_to_csv(cur, filename):
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%d.%m.%Y %H-%M-%S")
    sql = """COPY (SELECT * FROM "tripsDistance") TO STDOUT WITH DELIMITER ',' CSV HEADER;"""
    path = os.getcwd()
    out_dir = os.path.join(path,'pgOut',filename+' '+current_date+'.csv')
    with open(out_dir,'w') as f:
        cur.copy_expert(sql, f)

pg_export_to_csv(cur, "tripDistance")