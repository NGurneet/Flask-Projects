
import datetime


class Pet:
    def __init__(self):
        self.pid =0
        self.name=""
        self.age = 0
        self.weight = 0
        self.breed = ""
        self.gender = ""
        self.cid =0
        self.createdon =""

    def read_pet_data(self):
        self.name = input("Enter Pet Name: ")
        self.age = int(input("Enter Pet Age: "))
        self.weight = float(input("Enter Pet Weight: "))
        self.breed =input("Enter Pet Breed: ")
        self.gender = input("Enter Pet Gender: ")
        self.createdon =str(datetime.datetime.today())
        self.createdon = self.createdon[:self.createdon.rindex('.')]

    def get_insert_sql_query(self):
        sql = "insert into Pet values(null,'{name}',{age},{weight},'{breed}','{gender}','{cid}','{createdon}');".format_map(vars(self))
        return sql
    def get_pet_sql_query(self,cid ="",pid = ""):
        if len(str(cid))!=0:
            sql = "select * from Pet where cid = {}".format(cid)
        elif len(str(pid))!=0:
            sql = "select * from Pet where pid = {}".format(pid)
        else:
            sql = "select * from Pet "

        return sql

    def get_update_sql_query(self):

        sql = "update Pet set Pet_Name='{name}',Pet_Age={age},Pet_Weight={weight}, Pet_Breed='{breed}',Pet_Gender='{gender}' where pid ={pid} ;".format_map(vars(self))
        return sql


