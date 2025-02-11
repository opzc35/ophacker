import socket

def start_client(host='127.0.0.1', port=1145):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        hostname = socket.gethostname()
        ip_list = socket.gethostbyname_ex(hostname)[2]
        message = "connect;"+socket.gethostname()+":"+ip_list[0]
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print(f"收到数据: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_client()