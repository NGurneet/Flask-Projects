from DB_connector import DBHelper
from Customer_Data import Customer
from tabulate import tabulate
def customer_menu():
    customer = Customer()
    db =DBHelper()
    message = """
            >>Customer Menu
            ~~~~~~~~~~~~~~~~~~~~
            1: Add New Customer
            2: Update Existing Customer
            3: Delete Existing Customer
            4: View All Customers
            5: View Customer By Phone
            0: Quit
            ~~~~~~~~~~~~~~~~~~~~
            """
    print(message)
    choice = int(input("Enter Your Choice: "))
    while True:
        if choice == 1:
            customer.read_customer_data()
            print(vars(customer))

            sql = customer.get_insert_sql_query()
            db.execute(sql)
        elif choice == 2:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)
            """for row in rows:
                print(row)"""
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            customer.name = input("Enter New Name: ")
            if len(customer.name) == 0:
                customer.name = customer_fetched[1]
            customer.phone = input("Enter New Phone: ")
            if len(customer.phone) == 0:
                customer.phone = customer_fetched[2]
            customer.email = input("Enter New Email: ")
            if len(customer.email) == 0:
                customer.email = customer_fetched[3]
            customer.age = input("Enter New Age: ")
            if len(customer.age) == 0:
                customer.age = customer_fetched[4]
            else:
                customer.age = int(customer.age)
            customer.gender = input("Enter New Gender: ")
            if len(customer.gender) == 0:
                customer.gender = customer_fetched[5]

            sql = customer.get_update_sql_query()
            db.execute(sql)
            print(customer.name, "Updated...")
        elif choice == 3:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)
            """for row in rows:
                print(row)"""
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            customer_fetched = rows[0]
            cname = customer_fetched[1]
            delete_choice = input("Are you sure you want to delete (yes/no): ")
            if delete_choice.lower() == "yes":
                sql = customer.get_delete_sql_query()
                db.execute(sql)
                print("Customer Deleted...")
        elif choice == 4:
            sql = customer.get_customer_sql_query()
            rows = db.execute_select_sql(sql)
            # for row in rows:
            #    print(row)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
        elif choice == 5:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customer_sql_query(phone)
            rows = db.execute_select_sql(sql)
            """for row in rows:
                print(row)"""
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'CREATED_ON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            print("Thank You for Using VetsApp")
        elif choice == 0:
            break
        else:
            print("Invalid Choice!")
        print(message)
        choice = int(input("Enter Your Choice: "))