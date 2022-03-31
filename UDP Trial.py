import socket
import psychopy.core

UDP_IP = "192.168.137.2"
UDP_PORT = 9093
Remote_IP = "192.168.137.1"
Remote_Port = 9092
sock = socket.socket(
    socket.AF_INET, 
    socket.SOCK_DGRAM, 
    socket.INADDR_ANY)

sock.bind((UDP_IP, UDP_PORT))
AmpFactor = 0.000005
GammaFactor = 3.134
contrast = 1.0
gray = 50
inc = gray*contrast

sock.sendto(" ".join(["gamma", str(GammaFactor), "amp", str(AmpFactor)]), (Remote_IP, Remote_Port))


print(" ".join(["gamma", str(GammaFactor), "amp", str(AmpFactor)]))