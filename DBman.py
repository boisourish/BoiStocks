import sqlite3
dbconn = sqlite3.connect("users.db")
db = dbconn.cursor()

def create_user(name, email, hash):
    a = []
    if name and email and hash:
        try:
            a.append(name)
            a.append(email)
            a.append(hash)
            db.execute("INSERT INTO users(name, email, hash, money) values(?,?,?,10000);",a)
            return True
        except:
            return False
    else:
        return False

def get_hash(email):
    if email:
        try:
            user = db.execute("SELECT * FROM users WHERE email = ?;",email)
            return user["hash"]
        except:
            return 2
    else:
        return 1
