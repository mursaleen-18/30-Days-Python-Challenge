import socket

host = "google.com"
port = 80

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Create an HTTP GET request
request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
client_socket.sendall(request.encode())

# Receive the response
response = b""
while True:
    data = client_socket.recv(4096)
    if not data:
        break
    response += data

# Decode and print
print(response.decode(errors="ignore"))

client_socket.close()


import requests

url = "https://google.com"
response = requests.get(url)
print(response.text)
