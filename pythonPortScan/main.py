import socket


target_host = "127.0.0.1"
port_range = range(1, 100)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


for port in port_range:
    try:
        
        client_socket.connect((target_host, port))
        print(f"Port {port} is open")
        client_socket.close()
    except:
        
        print(f"Port {port} is closed")
