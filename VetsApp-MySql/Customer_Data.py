import datetime
class Customer:

    def __init__(self):
        self.cid = 0
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = 0
        self.gender = ""
        self.created_on = ""

    def read_customer_data(self):

        self.name = input("Enter Customer's Name: ")
        self.phone = input("Enter Customer's phone: ")
        self.email = input("Enter Customer's Email: ")
        self.age = int(input("Enter Customer's Age: "))
        self.gender = input("Enter Customer's Gender: ")
        self.created_on = str(datetime.datetime.today())
        self.created_on = self.created_on[:self.created_on.rindex('.')]
    def get_insert_sql_query(self):
        sql_query = "insert into Customer values(null,'{name}','{phone}','{email}',{age},'{gender}','{created_on}');".format_map(vars(self))
        return sql_query
    def get_customer_sql_query(self,phone =""):
        if len(phone)==0:
            sql_query = "select * from Customer"
        else:
            sql_query = "select * from Customer where Customer_Phone = '{}'".format(phone)
        return sql_query

    def get_delete_sql_query(self):
        sql_query = "delete from Customer where cid = {}".format(self.cid)
        return sql_query

    def get_update_sql_query(self):
        sql_query = "update Customer set Customer_Name='{name}',Customer_Phone='{phone}',Customer_Email='{email}', Customer_Age={age},Customer_Gender='{gender}' where cid ={cid} ;".format_map(vars(self))
        return sql_query
