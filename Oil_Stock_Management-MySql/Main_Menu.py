from Oil_Purchase_Data import Purchase
from Purchase_menu import purchase_menu
from DB_Oil_Connector import DBHelper

def main():
    db = DBHelper()
    purchase = Purchase()
    message ="""
    >>Main Menu
    -------------------
    1: Manage Purchase
    0: Exit
    -------------------
            """
    print(message)
    choice = int(input("Enter Choice: "))
    while True:
        if choice==1:
           purchase_menu()

        elif choice==0:
            print("~~~~~~~~~~~~~~~~~~~")
            print("Thanks For Using")
            print("~~~~~~~~~~~~~~~~~~~")
            break
        print(message)
        choice = int(input("Enter Choice: "))
        if choice ==0:
            bye_message = """
                **********************************
                    Thank You For Using
                **********************************"""
            print(bye_message)
            break
if __name__=="__main__":
    main()