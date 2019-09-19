import sqlite3
dbconn = sqlite3.connect("users.db")
db = dbconn.cursor()

class User:
    def __init__(self, email, hash):
        self.email = email
        self.hash = hash
        self.id = 0
        self.money = 0.0
        self.name = ""

    def chk_user(self):
        try:
            user = db.execute("SELECT * FROM users WHERE email = ?;",self.email)
            return self.hash == user.fetchone()[3]
        except:
            return False
            raise Exception("The database failed to reply correctly after being asked for a hash. BoiStocks/DBman/get_hash")

    def upd_user(self):
        if(self.chk_user()):
            self.id,self.name,self.email,k,self.money = db.execute("SELECT * FROM users WHERE email = ?;",self.email).fetchone()
            return True
        else:
            raise Exception(f"User {self.email} tried to log in with incorrect user details!")

    def change_money(self, amount):
        try:
            db.execute("UPDATE users SET money = money - ? WHERE id = ?;",[amount,self.id])
            return True
        except:
            return False



    





def db_save(): #saves the changes to the db
    dbconn.commit()

def db_save_exit(): #saves the changes to the db and closes the connection
    dbconn.commit()
    dbconn.close()

def create_user(name, email, hash): #creates a new user
    a = []
    if name and email and hash:
        try:
            a.append(name)
            a.append(email)
            a.append(hash)
            db.execute("INSERT INTO users(name, email, hash, money) values(?,?,?,10000);",a)
            db_save()
            return True
        except:
            raise Exception("The database failed to reply correctly after creating an user. BoiStocks/DBman/create_user")
            return False
    else:
        return False
        raise Exception("The function create_user received incorrect parameters. BoiStocks/DBman/create_user")

def get_hash(email):
    if email:
        try:
            user = db.execute("SELECT * FROM users WHERE email = ?;",email)
            return user.fetchone()[3]
        except:
            return 2
            raise Exception("The database failed to reply correctly after being asked for a hash. BoiStocks/DBman/get_hash")
    else:
        return 1
        raise Exception("The function received incorrect parameters. BoiStocks/DBman/get_hash")

def get_id(email):
    if email:
        try:
            user = db.execute("SELECT * FROM users WHERE email = ?;",email)
            return user.fetchone()[0]
        except:
            return 2
            raise Exception("The database failed to reply correctly after being asked for an id. BoiStocks/DBman/get_id")
    else:
        return 1
        raise Exception("The function received incorrect parameters. BoiStocks/DBman/get_id")

def get_money(id):
    try:
        return db.execute("SELECT * FROM users WHERE id = ?;",id).fetchone[4]
    except:
        return -1

def change_money(id, amount):
    #substracts amount from the money value of id
    try:
        db.execute("UPDATE users SET money = money - ? WHERE id = ?;",[amount,id])
        return True
    except
        return False
