from View import Engines
import threading
import time
print("Enter Video Link")
link='https://www.youtube.com/watch?v=VgXRSpKAFSw'

print('Enter the Duration of Video in seconds')
du=180

print("Enter Thread Count at a Time")
tc=2


bc=0
"""
###Dynamic IP
Dynamic_IP="110.77.168.82"
Dynamic_Port=8080
while(True):
    try:
        obj=[]
        t=[]
        bc=bc+1
        for i in range(tc):
            otemp=Engines()
            obj.append(otemp)
        for j in range(tc):
            th = threading.Thread(target=obj[j].View_Engine, args=(Dynamic_IP,Dynamic_Port,link,du))
            t.append(th)
            print("Thread- "+str(j)+" Started of Batch- ",str(bc))
            th.start()       

        for k in range(tc):
            t[k].join()
            print("Thread- "+str(k)+" Completed of Batch- "+str(bc))
        i=j=k=0
    except KeyboardInterrupt:
        print("Ended")
        break        

"""
## Static IP

proxy_list=[]
proxy_port=[]
file1 = open('proxies.txt','r')
for i in file1:
    ip,port=i.split(':')
    proxy_list.append(ip)
    proxy_port.append(int(port))

n=tc

while(proxy_list):
    obj=[]
    t=[]
    i=j=0
    for i in range(n):
        otemp=Engines()
        obj.append(otemp)
    for j in range(n):
        th = threading.Thread(target=obj[j].View_Engine, args=(proxy_list[j],proxy_port[j],link,du))
        proxy_list.pop(j)
        proxy_port.pop(j)
        t.append(th)       
        th.start()
        print("Thread Started")
        #time.sleep(10)    
    for thr in t:
        thr.join()
        print("Thread Complted")
        

print('------------All Thread Completed------------')    


