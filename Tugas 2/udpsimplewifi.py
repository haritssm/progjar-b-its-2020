
import socket

TARGET_IP = "192.168.1.123"
TARGET_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes('ABCDEFGHIJKLMNOPQRSTUV'.encode()),(TARGET_IP,TARGET_PORT))