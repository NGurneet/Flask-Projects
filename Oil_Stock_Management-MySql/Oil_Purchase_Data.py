import datetime
class Purchase:

    def __init__(self):
        self.pid = 0
        self.transaction_date =""
        self.product_name = ""
        self.product_price = 0.0
        self.quantity = 0
        self.amount_to_pay = 0
        self.purchase_payment_status = ""
        self.payment_clearance_date =""

    def set_product_name(self):
        product_list = """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Press '1' for: Oil Bottle 2 Ltr
        Press '2' for: Oil Bottle 5 Ltr
        Press '3' for: Enter a New Product
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        print(product_list)
        product_choice = int(input("Enter Your Choice here: "))
        while(True):
            if product_choice == 1:
                self.product_name = "Oil Bottle 2 Ltr"
                self.product_price = 360
                break
            elif product_choice == 2:
                self.product_name = "Oil Bottle 5 Ltr"
                self.product_price = 900
                break
            elif product_choice == 3:
                self.product_name = input("Enter the Product Name: ")
                break
            else:
                print("Sorry! Invalid Choice ")
            print(product_list)
            print("Enter the choice again")
            product_choice = int(input("Enter Your Choice here: "))

    def set_payment_status(self):
        payment_list = """
        ***********************
        Press 'P' for Paid 
        Press 'U' for Unpaid
        ***********************
        """
        print(payment_list)
        payment_status_choice = input("Enter Your Payment Choice here: ")
        while(True):
            if payment_status_choice =='p'or payment_status_choice =='P':
                self.purchase_payment_status = "Paid"
                break
            elif payment_status_choice =='u' or payment_status_choice =='U':
                self.purchase_payment_status = "Unpaid"
                break
            else:
                print("Sorry! Invalid Choice ")
                print("Enter the choice again")
                payment_status_choice = (input("Enter Your Payment Choice here: "))
        if self.purchase_payment_status =="Paid":
            self.payment_clearance_date = input("Enter the Transaction Clearence Date (YYYY-MM-DD): ")
        else:
            self.payment_clearance_date ="Payment Pending"

    def read_purchase_data(self):

        self.set_product_name()
        self.transaction_date = str(datetime.datetime.today())
        self.transaction_date = self.transaction_date[:self.transaction_date.rindex('.')]
        self.quantity = int(input("Enter the Quantity: "))
        self.amount_to_pay = self.product_price*self.quantity
        self.set_payment_status()

    def get_insert_sql_query(self):

        sql = "insert into Purchase values(null,'{transaction_date}','{product_name}',{product_price},{quantity},{amount_to_pay},'{purchase_payment_status}','{payment_clearance_date}')".format_map(vars(self))
        return sql

    def get_select_sql_query(self):

        sql = 'select *  from Purchase;'
        return sql

    def get_update_sql_query(self):
        sql = "update Purchase set Product_Name = '{product_name}',Quantity ={quantity},Purchase_Payment_Status='{purchase_payment_status}',Payment_Clearence_Date = '{payment_clearance_date}' where Pid ={pid};' ".format_map(vars(self))
        return sql
"""
CREATE TABLE Purchase(
    Pid int primary key auto_increment,
    Transaction_Date datetime,
    Product_Name text,
    Product_Price int,
    Quantity int,
    Amount int ,
    Purchase_Payment_Status text,
    Payment_Clearence_Date text
    );"""

