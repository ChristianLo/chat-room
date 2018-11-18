#!/usr/local/bin/python3

import os
import random
import socket
import threading

from rand_users import GenerateRandom

list_clients = []
client_names = {}
random_names = GenerateRandom.Witcher().characters()


def conectados():
    os.system('clear')
    print("Conectados : ", len(list_clients))
    if len(client_names) >0:
        print(*[b for b in client_names.values()], sep='\n')


def hilo(address):
    cliente, direccion = address
    name = random.choice(random_names)

    if cliente not in list_clients:
        list_clients.append(cliente)
        client_names[cliente] = name

    with cliente:
        mensaje = str(name) + " ha ingersado"
        print(mensaje)
        cliente.send(str("name,{}".format(name)).encode())
        sendall(cliente, mensaje.encode())
        while True:
            try:
                mensaje, addr = cliente.recvfrom(1024)
                if mensaje:
                    # msj = str(mensaje) + " : " + str(cliente)
                    msj = str(name) + ":" + mensaje.decode()
                    # print(name, "dijo: ", mensaje.decode().strip('\n'))
                    sendall(cliente, msj.encode())
                else:
                    remove(cliente)
                    conectados()
                    sendall(cliente, "{} se ha desconectado".format(name).encode())
                    break
            except KeyboardInterrupt:
                break


def sendall(conn, msj):
    for clients in list_clients:
        if clients != conn:
            try:
                clients.send(msj)
            except:
                clients.close()

                remove(clients)


def remove(conn):
    if conn in list_clients:
        list_clients.remove(conn)
        client_names.pop(conn)


HOST = '0.0.0.0'
PORT = 15000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))

    print("Esperando una conexion...")

    server.listen(100)

    while True:
        conectados()
        conn, addr = server.accept()
        threading.Thread(target=hilo, args=((conn, addr),)).start()
    conn.close()
    server.close()
