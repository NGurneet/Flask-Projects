import mysql.connector as db

class DBHelper:

    def __init__(self):
        self.connection = db.connect(
                        user = "root",
                        password ="Root",
                        host="127.0.0.1",
                        database = "vets_app"
        )

        #step 2: obtain Cursor to perform SQL query
        self.cursor = self.connection.cursor()
        print("[DBHelper] Connection Created and Cursor Obtained")
    def execute(self,sql):
        print("[DBHelper] Executing Query:",sql,)
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] Query Executed Successfully...]")
    def execute_select_sql(self,sql):
        print("[DBHelper] Executing Query:", sql, )
        self.cursor.execute(sql)
        rows= self.cursor.fetchall()
        print("[DBHelper] Query Executed Successfully...]")
        return rows





