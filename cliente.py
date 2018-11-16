import os
import select
import socket
import sys

ip = '127.0.0.1'
puerto = 15000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((ip, puerto))
    os.system('clear')
    _, name = cliente.recv(2048).decode().strip().split(',')
    print("Welcome a chat-room of Witcher, your name is '{}'\n".format(name))

    while True:
        try:
            socket_list = [sys.stdin, cliente]
            read_socket, write_socket, error_socket = select.select(socket_list, [], [])

            for socks in read_socket:
                if socks is cliente:
                    message = socks.recv(2028).decode().strip('\n')
                    if message:
                        print(message)
                    else:
                        raise Exception
                else:
                    message = sys.stdin.readline().strip()

                    if message.lower() == "quit":
                        raise Exception

                    cliente.send(message.encode())
                    sys.stdout.write("{} : ".format(name) + message + "\n")
                    sys.stdout.flush()
        except:
            print("sesion terminada")
            break
    cliente.close()
