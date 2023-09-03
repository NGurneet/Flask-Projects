from Pet_Data import Pet
from Customer_Data import Customer
from DB_connector import DBHelper
from tabulate import tabulate
from Consultation_Data import  Consultation
def consultation_menu():
    db=DBHelper()
    customer =Customer()
    consultation  =Consultation()
    pet = Pet()

    message = """
            >>Consultation Menu
            ~~~~~~~~~~~~~~~~~~~~
            1: Add New consultation
            2: Update consultation
            3: View Consultation of Customers 
            4: View All consultation
            5: View Consultations by Customer's Pet
            0: Quit
            ~~~~~~~~~~~~~~~~~~~~
            """
    print(message)
    choice = int(input("Enter Your Choice: "))
    while True:
        if choice == 1:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)

            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            customer_fetched = rows[0]
            pet.cid = customer_fetched[0]
            consultation.cid = customer_fetched[0]
            sql = pet.get_pet_sql_query(cid=str(pet.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            if len(rows)==1:
                pet.pid =rows[0][0]
            else:
                pet.pid =int(input("Enter Pid: "))

            consultation.pid = pet.pid
            print(vars(consultation))
            consultation.read_consultation_data()
            sql = consultation.get_insert_sql_query()
            print(vars(consultation))
            db.execute(sql)

        elif choice == 2:
            phone = input("Enter Customer's Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            sql = pet.get_pet_sql_query(rows[0][0])
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            if len(rows) == 1:
                consultation.pid = rows[0][0]
            else:
                consultation.pid = input("Enter Pid : ")
            sql = consultation.get_consult_sql_query(pid=consultation.pid)
            rows = db.execute_select_sql(sql)
            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPERATURE', 'MEDICINES', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
        elif choice == 3:
            phone =input("Enter Customer's Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            consultation.cid = rows[0][0]
            sql = consultation.get_consult_sql_query(cid=consultation.cid)
            rows = db.execute_select_sql(sql)
            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPERATURE', 'MEDICINES', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))


        elif choice == 4:

            sql = consultation.get_consult_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ['CNID', 'CID','PID','PROBLEM', 'HEARTRATE', 'TEMPERATURE', 'MEDICINES', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 5:
            phone = input("Enter Customer's Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            sql = pet.get_pet_sql_query(rows[0][0])
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            if len(rows)==1:
                consultation.pid = rows[0][0]
            else:
                consultation.pid =input("Enter Pid : ")
            sql =consultation.get_consult_sql_query(pid = consultation.pid)
            rows = db.execute_select_sql(sql)
            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPERATURE', 'MEDICINES', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))



        elif choice == 0:
            break
        else:
            print("Invalid Choice!")
        print(message)
        choice = int(input("Enter Your Choice: "))