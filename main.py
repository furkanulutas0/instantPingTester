import time
from pythonping import ping
ipadresi = 0#ipadresiniz
i = 0 
while(True):
    i+=1
    time.sleep(1/2)
    print(f"time {i}")
    ping(ipadresi, verbose = True)


