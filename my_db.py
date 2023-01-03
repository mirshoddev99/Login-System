import sqlite3
import hashlib

connect = sqlite3.connect("userdata.db")
cur = connect.cursor()

cur.execute("""
CREATE TABLE userdata (
        id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL, 
        password VARCHAR(255) NOT NULL
    )
""")

user1, password1 = "mike256", hashlib.sha256("mikepassword".encode()).hexdigest()
user2, password2 = "mirshod99", hashlib.sha256("my_password".encode()).hexdigest()
user3, password3 = "admin99", hashlib.sha256("admin1999".encode()).hexdigest()
user4, password4 = "python3", hashlib.sha256("python_password".encode()).hexdigest()


cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (user1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (user2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (user3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (user4, password4))

connect.commit()
connect.close()
print("Table created successfully")
