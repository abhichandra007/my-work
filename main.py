import psycopg2
class Comp:
    def __init__(self,table) :
        self.connection = psycopg2.connect(user='postgres', password='1234', host='localhost', port=5432, database='northwind')
        self.table = table
        self.primary_key = ''


    def create_table(self, values={'name': 'varchar(50)', 'location': 'varchar(50)', 'id': 'int'}, pk=''):
        self.primary_key = pk
        values[self.primary_key] = values[self.primary_key] + ' PRIMARY KEY'
        cursor=self.connection.cursor()
        res = []
        for i, j in values.items():
            res.append(str(i)+' '+str(j))
        query = f"""create table {self.table} ({', '.join(res)})"""
        print(query)
        cursor.execute(query)
        self.connection.commit
        print("table created successfully")  


    def insert_table(self, query_details):
        cursor = self.connection.cursor()
        query_value = ''
        columns = ''
        for _, value in query_details.items():
            columns = ', '.join(list(value.keys()))
            query_value = ', '.join(list(value.values()))
        query = f"""insert into {self.table} ({columns}) values ({query_value})"""

        cursor.execute(query)
        self.connection.commit()
        return "Table inserted successfully"


    def update_table(self, values):
        cursor = self.connection.cursor()
        res = []
        for i, j in values.items():
            res.append(str(i) + " = '" + str(j) + "'")
        set = ", ".join(res)
        query = f"update {self.table} set {set}"
        cursor.execute(query)
        self.connection.commit()
        print( "Table updated successfully")



    def delete_table(self, values):
        cursor = self.connection.cursor()
        res= []
        for i, j in values.items():
            res.append(str(i) + " = '" + str(j) + "'")
        where = " and ".join(res)
        query = f"delete from {self.table} where {where}"
        cursor.execute(query)
        self.connection.commit()
        print("table deleted successfully")
            
            


Comp=Comp('table3')

Comp.create_table(values={'name': 'varchar(50)', 'adress': 'varchar(50)', 'phone': 'int'}, pk='phone')

query_details = {123:{'name':'akhil','adress': 'hyd'},124:{'name':'adhi','adress': 'hyd'},125:{'name':'ravi','adress':'rr'},126:{'name':'suresh','adress':'nzpt'}}
Comp.insert_table(query_details)

# Comp.update_table({})

# Comp.delete_table({'location': 'hyd'})
