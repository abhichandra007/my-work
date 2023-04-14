import psycopg2
# import mysql.connector
import pandas as pd
class Comp:
    def __init__(self,table) :
     
            self.connection = psycopg2.connect(user='postgres', password='1234', host='localhost', port=5432, database='northwind')
            self.table = table
            self.primary_key = ''
    

    def create_table(self, values={'name': 'varchar(50)', 'address': 'varchar(50)', 'phone': 'int'}, pk=''):
        self.primary_key = pk
        values[self.primary_key] = values[self.primary_key] + ' PRIMARY KEY'
        cursor=self.connection.cursor()
        res = []
        for i, j in values.items():
            res.append(str(i)+' '+str(j))
        query = f"""create table {self.table} ({', '.join(res)})"""
        print(query)
        try:
            cursor.execute(query)
            self.connection.commit()
            print("table created successfully")
        except Exception as e:
            print("Error creating table:", e)  


    def insert_table(self,table):

        cursor = self.connection.cursor()
        query = f"""insert into {table} values ('oneplus', 'hyd',123), ('mi', 'rr',345), ('sy', 'ben',2345), ('da', 'jksf',986), ('uhfsuah', 'jhbfsd',7654), ('js', 'jusafdn',7543)"""
        cursor.execute(query)
        self.connection.commit()
        print("Table inserted successfully")

    # def update_table(self, values):
         
    #         cursor = self.connection.cursor()
    #         res = []
    #         for i, j in values.items():
    #           res.append(str(i) + " = '" + str(j) + "'")
    #         set = ", ".join(res)
    #         query = f"update {self.table} set {set}"
    #         try:
    #            cursor.execute(query)
    #            self.connection.commit()
    #            print( "Table updated successfully")
    #         except Exception as e:
    #             print(f"Error while updating table: {e}")
    #             self.connection.rollback()

    # def delete_table(self, values):
        
    #         cursor = self.connection.cursor()
    #         res= []
    #         for i, j in values.items():
    #           res.append(str(i) + " = '" + str(j) + "'")
    #         where = " and ".join(res)
    #         query = f"delete from {self.table} where {where}"
    #         try:
    #             cursor.execute(query)
    #             self.connection.commit()
    #             print("table deleted successfully")
    #         except Exception as e:
    #             print(f"Error while deleting table")



class TableReport:
    def __init__(self, table, user, password, host, port, database):
        self.table = table
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        

    # def connect(self):
    #     try:
    #         # Connect to PostgreSQL or MySQL database
    #         if self.database.upper() == 'POSTGRESQL':
    #             self.conn = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.database)
    #             print("PostgreSQL Database connected successfully")
    #         elif self.database.upper() == 'MYSQL':
    #             self.conn = mysql.connector.connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.database)
    #             print("MySQL Database connected successfully")
    #         else:
    #             print("Incorrect value entered for database. Please restart the program.")
    #     except Exception as e:
    #         print(f"Connection Failure: {e}")

    def get_data_type(self):
        try:
            query = f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{self.table}'"
            df = pd.read_sql(query,Comp.__init__)
            print("Data Types:")
            print(df)
        except Exception as e:
            print(f"Error while getting data types: {e}")

    # def get_size(self):
    #     try:
    #         query = f"SELECT COUNT(*) AS total_rows, pg_size_pretty(pg_total_relation_size('{self.table}')) AS total_size FROM {self.table}"
    #         df = pd.read_sql(query, self.conn)
    #         print("Size:")
    #         print(df)
    #     except Exception as e:
    #         print(f"Error while getting table size: {e}")

    # def get_null_values(self):
    #     try:
    #         query = f"SELECT column_name, COUNT(*) AS null_count FROM {self.table} WHERE column_name IS NULL GROUP BY column_name"
    #         df = pd.read_sql(query, self.conn)
    #         print("Null Values:")
    #         print(df)
    #     except Exception as e:
    #         print(f"Error while getting null values: {e}")

    # def get_duplicate_values(self):
    #     try:
    #         query = f"SELECT COUNT(*) AS duplicate_count FROM {self.table} GROUP BY column1, column2 HAVING COUNT(*) > 1"
    #         df = pd.read_sql(query, self.conn)
    #         print("Duplicate Values:")
    #         print(df)
    #     except Exception as e:
    #         print(f"Error while getting duplicate values: {e}")

    # def get_primary_keys(self):
    #     try:
    #         query = f"SELECT column_name FROM information_schema.key_column_usage WHERE table_name = '{self.table}' AND constraint_name LIKE 'pk_%'"
    #         df = pd.read_sql(query, self.conn)
    #         print("Primary Keys:")
    #         print(df)
    #     except Exception as e:
    #         print(f"Error while getting primary keys: {e}")

    def generate_report(self):
    #     # self.connect()
        self.get_data_type()
    #     self.get_size()
    #     self.get_null_values()
    #     self.get_duplicate_values()
    #     self.get_primary_keys()
         
              
    



Comp=Comp('revanth78070')


Comp.create_table(pk='phone')
Comp.insert_table('revanth78070')
table_report = TableReport(table='revanth78070', user='postgres', password='1234', host='localhost', port=5432, database='northwind')
table_report.generate_report()
# Comp.update_table({})
# Comp.delete_table({'address': 'hyd'})  
