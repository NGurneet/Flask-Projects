from Oil_Purchase_Data import Purchase
from DB_Oil_Connector import DBHelper
from tabulate import tabulate

def purchase_menu():
    db = DBHelper()
    purchase = Purchase()
    messsage ="""
            >>Purchase Menu
            1: Add a New Purchase Transaction
            2: Update a Purchase Transaction
            3: Update Payment Status
            4: Show all Transaction
            0: Exit from Purchase Menu
            """
    print(messsage)
    choice =int(input("Enter Choice: "))

    while True:
        if choice==1:

            purchase.read_purchase_data()
            print(vars(purchase))
            sql = purchase.get_insert_sql_query()
            db.execute(sql)


        if choice==2:
            sql = purchase.get_select_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ["PID", "TRANSACTION DATE", "PRODUCT NAME", "PRODUCT_PRICE", "QUANTITY", "AMOUNT_TO_PAY",
                       "PAYMENT STATUS", "PAYMENT CLEARANCE DATE"]
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            purchase.pid = int(input("Enter The PID of the transaction to update: "))
            purchase_fetched = rows[0]
            print("Enter Below Those Details you want to update ")
            print("If you don't want to update Press Enter to skip update that column...")
            set_name_choice = int(input("Press '1' to update Name OR Press '0' to skip update Name"))
            if set_name_choice ==1:
                purchase.set_product_name()

            if len(purchase.product_name)==0:
                purchase.product_name = purchase_fetched[2]

            purchase.quantity = input("Enter Product Quantity: ")
            if len(purchase.quantity)==0:
                purchase.quantity = purchase_fetched[4]
            update_paymenent_status =int(input("Press '1' to update Payment Status OR Press '0' to skip update Payment Status: "))
            if update_paymenent_status==1:
                purchase.set_payment_status()
            if len(purchase.purchase_payment_status)==0:
                purchase.purchase_payment_status = purchase_fetched[6]
            if update_paymenent_status !=1:
                purchase.payment_clearance_date = input("Enter Payment Clearance Date : ")
                if len(purchase.payment_clearance_date)==0:
                    purchase.payment_clearance_date = purchase_fetched[7]
            sql = purchase.get_update_sql_query()
            db.execute(sql)
            print(" Purchase Updated...")

        if choice==3:
            pass
        if choice==4:
            sql = purchase.get_select_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ["PID","TRANSACTION DATE","PRODUCT NAME","PRODUCT_PRICE","QUANTITY","AMOUNT_TO_PAY","PAYMENT STATUS","PAYMENT CLEARANCE DATE"]
            print(tabulate(rows , headers=columns,tablefmt="grid"))
        if choice==0:
            print("~~~~~~~~~~~~~~~~~~~")
            print("Thanks For Using")
            print("~~~~~~~~~~~~~~~~~~~")
        print(messsage)
        choice = int(input("Enter Choice: "))
        if choice==0:
            break


