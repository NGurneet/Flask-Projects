from Pet_Data import Pet
from Customer_Data import Customer
from DB_connector import DBHelper
from tabulate import tabulate

def main():
    db = DBHelper()
    print("Welcome to VetsApp")
    pet =Pet()
    message = """
            ~~~~~~~~~~~~~~~~~~~~
            1: Add New Pet
            2: Update Existing Pet
            4: View All Pets
            5: View Customer's Pet
            0: Quit
            ~~~~~~~~~~~~~~~~~~~~
            """
    print(message)
    choice =int(input("Enter Your Choice: "))
    customer =Customer()
    while True:
        if choice==1:

            phone = input("Enter Customer Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)
            """for row in rows:
                print(row)"""
            columns=['PID','NAME','AGE','WEIGHT','BREED','GENDER','CID','CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            customer_fetched = rows[0]
            pet.cid = customer_fetched[0]
            pet.read_pet_data()
            print(vars(pet))

            sql = pet.get_insert_sql_query()
            db.execute(sql)
            print("Data Saved Successfully...")
        elif choice ==2:
            pass
        elif choice==4:
            sql =pet.get_pet_sql_query()
            rows =db.execute_select_sql(sql)
            columns=['PID','NAME','AGE','WEIGHT','BREED','GENDER','CID','CREATED_ON']
            print(tabulate(rows,headers=columns,tablefmt="grid"))
        elif choice==5:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)

            columns=['PID','NAME','AGE','WEIGHT','BREED','GENDER','CID','CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            customer_fetched = rows[0]
            pet.cid = customer_fetched[0]
        elif choice==0:
            print("Thanks For Using VetsApp")
            break
        print(message)
        choice = int(input("Enter Your Choice: "))

if __name__=="__main__":
    main()