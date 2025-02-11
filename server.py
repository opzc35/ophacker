import socket
import json
import atexit
import threading
import os
connect_list = []
def save_connect_list():
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(connect_list, f, indent=4)
    print("connect_list已保存到save.json")
atexit.register(save_connect_list)
def new_connect(ip, hostname):
    connect_list.append({"ip": ip, "hostname": hostname})
def action(s):
    s = s.split(';')
    if s[0] == 'connect':
        print('开始连接' + s[1])
        print('\033[33m正在解析目标字符串\033[0m')
        info = s[1].split(':')
        ip = info[1]
        hostname = info[0]
        print('\033[31m解析成功，即将连接至ip:' + ip + ',hostname:' + hostname + '\033[0m')
        print('\033[32m连接成功\033[0m')
        new_connect(ip, hostname)
def start_server(host='127.0.0.1', port=1145):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"服务器正在 {host}:{port} 上监听...")
        conn, addr = server_socket.accept()
        with conn:
            print(f"已连接到 {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"收到数据: {data.decode('utf-8')}")
                action(data.decode('utf-8'))
                conn.sendall(b'connect accept')
def main():
    global connect_list
    print('欢迎使用op-hackerJC工具')
    while True:
        try:
            op = input("请输入你要执行的操作: ")
            if op == "get_connect_list":
                print('\033[33m开始输出\033[0m')
                for i in connect_list:
                    print(i)
            elif op == "recovery_connect_list":
                print('\033[33m开始还原连接记录\033[0m')
                with open('save.json', 'r', encoding="utf-8") as f:
                    info = json.load(f)
                connect_list = info
                print('\033[32m还原成功\033[0m')
        except UnicodeDecodeError as e:
            print(f"输入错误，无法解码：{e}")
            continue
if __name__ == "__main__":
    os.system('chcp 65001')
    thread = threading.Thread(target=start_server)
    thread.start()
    thread2 = threading.Thread(target=main)
    thread2.start()
