from Pet_Data import Pet
from Customer_Data import Customer
from DB_connector import DBHelper
from tabulate import tabulate
def pets_menu():
    pet =Pet()
    customer =Customer()
    db=DBHelper()
    message = """
            >>Pets Menu
            ~~~~~~~~~~~~~~~~~~~~
            1: Add New Pet
            2: Update Existing Pet
            3: Delete Existing Pet
            4: View All Pets
            5: View pet by Customer
            0: Quit
            ~~~~~~~~~~~~~~~~~~~~
            """
    print(message)
    choice = int(input("Enter Your Choice: "))
    while True:
        if choice == 1:
            pet.read_pet_data()

            phone = input("Enter Customer Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)

            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            customer_fetched = rows[0]
            pet.cid = customer_fetched[0]
            print(vars(pet))


            sql = pet.get_insert_sql_query()
            db.execute(sql)
            print("Data Saved Successfully...")
        elif choice == 2:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)

            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER','CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            customer_fetched = rows[0]
            pet.cid = customer_fetched[0]

            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATED_ON']
            sql = pet.get_pet_sql_query(cid=str(pet.cid))
            rows = db.execute_select_sql(sql)
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            pet_fetched = rows[0]
            print(pet_fetched)
            if len(rows)==1:
                pet.pid = pet_fetched[0]
            else:

                pet.pid = input("Enter Pid of Pet: ")
            sql =pet.get_pet_sql_query(pid=pet.pid)
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            pet_fetched = rows[0]
            pet.name = input("Enter New Name: ")
            if len(pet.name) == 0:
                pet.name = rows[0][1]
            pet.age = input("Enter New age: ")
            if len(pet.age) == 0:
                pet.age = rows[0][2]
            pet.weight = input("Enter New weight: ")
            """else:
                pet.age = int(pet.age)"""

            if len(pet.weight) == 0:
                pet.weight = rows[0][3]
            pet.breed = input("Enter New breed: ")
            if len(pet.breed) == 0:
                pet.breed = rows[0][4]
            pet.gender = input("Enter New Gender: ")
            if len(pet.gender) == 0:
                pet.gender = rows[0][5]

            sql = pet.get_update_sql_query()
            db.execute(sql)
            print(pet.name, "Updated...")

        elif choice == 3:
            pass
        elif choice == 4:
            sql = pet.get_pet_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
        elif choice == 5:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)

            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            customer_fetched = rows[0]
            pet.cid = customer_fetched[0]
            sql =pet.get_pet_sql_query(cid=str(pet.cid))
            rows =db.execute_select_sql(sql)
            print(tabulate(rows, headers=columns, tablefmt="grid"))
        elif choice == 0:
            break
        else:
            print("Invalid Choice!")
        print(message)
        choice = int(input("Enter Your Choice: "))
