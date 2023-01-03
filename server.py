import socket
import threading
import sqlite3
import hashlib
from creds import host, port


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


def hand_client(cl):
    cl.send("Username: ".encode())
    username_res = cl.recv(1024).decode()
    cl.send("Password: ".encode())
    password_res = cl.recv(1024)
    password_res = hashlib.sha256(password_res).hexdigest()

    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM userdata WHERE username = ? AND password = ?", (username_res, password_res))

    if cur.fetchall():
        cl.send("You have logged in successfully!!!".encode())
    else:
        cl.send("Login failed".encode())


while True:
    client, address = server.accept()
    thread = threading.Thread(target=hand_client, args=(client,))
    thread.start()
