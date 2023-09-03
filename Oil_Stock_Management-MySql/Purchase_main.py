from Oil_Purchase_Data import Purchase
from DB_Oil_Connector import DBHelper

def main():
    db =DBHelper()
    purchase = Purchase()
    purchase.read_purchase_data()
    print(vars(purchase))
    sql = purchase.get_insert_sql_query()
    db.execute(sql)



if __name__ =="__main__":
    main()