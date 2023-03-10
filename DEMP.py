import psycopg2
class Comp:
    def __init__(self,table) :
        self.connection = psycopg2.connect(user='postgres', password='1234', host='localhost', port=5432, database='northwind')
        self.table = table


    def create_table(self, values={'name': 'varchar(50)', 'adress': 'varchar(50)', 'phone': 'int'}):

        cursor=self.connection.cursor()
        res = []
        for i, j in values.items():
            res.append(str(i)+' '+str(j))

        query = f"""create table {self.table} ({',  '.join(res)})"""
        cursor.execute(query)
        self.connection.commit
        print("table created successfully")  


    def insert_table(self,table):
        cursor = self.connection.cursor()
        query = f"""insert into {table} values ('oneplus', 'hyd'), ('mi', 'rr'), ('sy', 'ben'), ('da', 'jksf'), ('uhfsuah', 'jhbfsd'), ('js', 'jusafdn')"""
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





    def delete_table(self):
        cursor = self.connection.cursor()
        query = f"delete from {self.table}"
        cursor.execute(query)
        self.connection.commit()
        print( "All rows deleted successfully")
    



 




    


    









Comp=Comp('table1')

Comp.create_table()

Comp.insert_table('table1')

Comp.update_table({'name': 'updated name'})

Comp.delete_table({'address' :'hyd'})