#!/usr/bin/python2

"""
Networks Lab 3: UDP Socket Programming

Server code.
"""

from socket import *
import time

if __name__ == "__main__":
    print ("Server started")
    sock = socket(AF_INET, SOCK_DGRAM)
    #sock.bind(('0.0.0.0', 5555))
    sock.bind(('localhost', 5555))
    count = 0
    et=0
    st=0
    end_flg=0
    st_flg=0
    str_data = ""
    while True:
        data,addrs = sock.recvfrom(4096)
        str_data = data.decode()
        header_id = 'udpid' + str(count)
        header_id_length = len(header_id)
        if (header_id_length <= 9):
            m_h = 'udpid' + ("0" * (9 - header_id_length)) + str(count)
        rc_header = str_data[:9]
        if(m_h !=rc_header and end_flg==0):
            print("Error data")
            print(rc_header)
            print(m_h)
            break
        if(m_h ==rc_header and end_flg==0):
            count+=1

        if("udpid0" in str_data and st_flg==0):
            start_time = time.time()
            st = start_time
            st_flg=1

        if("udpid1000" in str_data):
            end_time = time.time()
            et = end_time
            print (et-st)
            print ("Restart checking! Please restart server!")
            end_flg=1
            break


