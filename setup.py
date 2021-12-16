#Import all requirment modules
import socket
#from datetime import datetime
from datetime import datetime
#for threading
import threading
from queue import Queue

#it is use for prevent duplicate entries form shared variable
print_lock = threading.Lock()

#Enter Host to scan
host = input("Enter hostname to scanning: ")
ip = socket.gethostbyname(host) #Translate DNS to IP

#These three lines are just added for look and feel
print("-" * 80)
print("         Please wait while scanning the Host --------->", ip)
print("-" * 80)

#Get Starting Time
t1 = datetime.now
print (t1)

#Port Scanning
def scan(port):
    
    try:
    # for port in range(1,65535):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Create Sock Stream
        result = sock.connect_ex((ip,port))
        if result == 0:
            #if a socket is listening it will print out the port number
            print("\n Port %d Is Open ---------------->" %(port))
            sock.close()
        else:
            print("\n Port %d Is Close :-( " %(port))
    except:
        pass

#Create a queueu by
q = Queue()

#Create threader function
def threader():
    while True:
        worker = q.get()
        scan(worker) #scan is a function & it run the job with the available worker in queue
        q.task_done()

#writing for loop for number of thread to allow
for y in range(60):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
    
for worker in range(1,65535): #Scan all ports from 1 to 65535
    q.put(worker)
    
#thread will join after thread termination
q.join()

#calculate end of exec time
t2 = datetime.now

#calculate the difference of time
total = t2 -t1
print("Total Scanning Time: ",total)