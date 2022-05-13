import socket 
HOST = "172.20.10.3" #cau hinh address su dung
SERVER_PORT = 65432 #cau hinh port su dung
FORMAT ="utf8" #utf-8 la 1 cach thuc encoding dien dat bang ma unicode tren bo nho
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #cau hinh socket
client.connect( (HOST, SERVER_PORT))    #ket noi den server
print("Connected to the server")
print("Client address: ",client.getsockname())
print("Nhap 2 so x va y:")
x=int(input())
y=int(input())
#sendall: gui du lieu len server
#recv: doc du lieu server tra ve
client.sendall(str(x).encode(FORMAT))
client.sendall(str(y).encode(FORMAT))
tong=client.recv(1024).decode(FORMAT)
client.sendall(tong.encode(FORMAT))
hieu=client.recv(1024).decode(FORMAT)
client.sendall(hieu.encode(FORMAT))
tich=client.recv(1024).decode(FORMAT)
client.sendall(tich.encode(FORMAT))
thuong=client.recv(1024).decode(FORMAT)
client.sendall(thuong.encode(FORMAT))
print("Tong 2 so la:" , tong)
print("Hieu 2 so la:" , hieu)
print("Tich 2 so la:" , tich)
print("Thuong 2 so la:" , thuong)
client.close() #ket thuc