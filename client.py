import socket

host = "192.168.1.100"
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


username_msg = client.recv(1024).decode()
msg = input(username_msg)
client.send(msg.encode())
password_msg = client.recv(1024).decode()
msg = input(password_msg)
client.send(msg.encode())
final_msg = client.recv(1024).decode()
print(final_msg)
