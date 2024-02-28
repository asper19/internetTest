from pythonping import ping 
from io import StringIO
import time
import os
import socket

while (True):

    myTime0 = time.localtime()
    fileTitle = time.strftime('%Y%m%d', myTime0)
    file = open(os.path.join("logs", fileTitle), 'a')

    with open(os.path.join("logs", fileTitle), 'a') as file :
        while(fileTitle == time.strftime('%Y%m%d', myTime0) ) :
            
            try :
                myTime1 = time.localtime()
                ResponseList = ping('8.8.8.8', verbose=True, interval=2, count=10)
                myTime2 = time.localtime()
                iso1 = time.strftime('%Y-%m-%dT%H:%M:%S', myTime1)
                iso2 = time.strftime('%Y-%m-%dT%H:%M:%S', myTime2)
                file.write(f'{iso1}, {iso2}, {ResponseList.success(2)}, {ResponseList.rtt_avg_ms}, {ResponseList.stats_success_ratio} \n')
            except socket.error:
                file.write(f'{iso1}, {iso2}, False, SocketError, SocketError\n')

            myTime0 = time.localtime()