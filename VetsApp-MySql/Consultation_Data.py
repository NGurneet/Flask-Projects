import datetime

class Consultation:

    def __init__(self):
        self.cnid = 0
        self.cid = 0
        self.pid = 0
        self.problem = ""
        self.heartrate = 0
        self.temperature = 98.8
        self.medicines = ""
        self.created_on = ""

    def read_consultation_data(self):
        self.problem = input("ENter Problem: ")
        self.heartrate = int(input("ENter HeartRate: "))
        self.temperature = float(input("ENter Temperature: "))
        self.medicines = input("ENter Medicines: ")
        self.createdon = str(datetime.datetime.today())
        self.createdon = self.createdon[:self.createdon.rindex('.')]

    """
    create table Consultation(
        cnid int primary key auto_increment,
        cid int ,
        pid int,
        problem text,
        heartrate int,
        temperature float,
        medicines text ,
        created_on datetime,
        FOREIGN KEY (cid) REFERENCES Customer(cid),
        FOREIGN KEY (pid) REFERENCES Pet(pid)
        );
    """
    def get_insert_sql_query(self):
        sql = "insert into Consultation values(null,{cid},{pid},'{problem}',{heartrate},{temperature},'{medicines}','{createdon}');".format_map(vars(self))
        return sql

    def get_consult_sql_query(self, pid="",cid ="",created_on =""):

        sql = "select * from consultation"
        if len(str(pid)) != 0:
            sql = "select * from consultation where pid = {}".format(pid)
        if len(str(cid)) != 0:
            sql = "select * from consultation where cid = {}".format(cid)
        if len(created_on) != 0:
            sql = "select * from consultation where created_on = {}".format(created_on)


        return sql

    """def get_update_sql_query(self):
        sql = update Consultation set Problem='{PROBLEM}'"""