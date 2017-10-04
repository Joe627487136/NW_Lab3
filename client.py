#!/usr/bin/python2

"""
Networks Lab 3: UDP Socket Programming

Client code.
"""

from socket import *
import argparse
import datetime, time, threading





if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', type=float, dest='rate',
        help='Packet rate in Mbps (eg; -r 1.5 is 1.5 Mbps)')

    args = parser.parse_args()

    if args.rate == None:
        print("USAGE:")
        print("python2 client.py -r 3.0:")
    else:
        print("Client rate is {} Mbps.".format(args.rate))
        count = 0
        sock = socket(AF_INET, SOCK_DGRAM)
        #server_address = ('10.0.0.2', 5555)
        server_address = ('localhost', 5555)
        start_time = time.time()
        outfloat = 0
        outfloat_flag = 0
        tst=0

        def g_tick():
            t = time.time()
            count2 = 0
            while True:
                count2 += 1
                yield max(t + count2 * 1/1000 - time.time(), 0)


        g = g_tick()
        while(count<=1000):
            header_id = 'udpid' + str(count)
            header_id_length = len(header_id)
            if(header_id_length<=9):
                m_h = 'udpid' + ("0"*(9-header_id_length)) + str(count)
            message = 'X' * int((10 ** 3 * args.rate)-9)
            final_msg = (m_h+message).encode()
            if(len(final_msg)!=10 ** 3 * args.rate):
                print ("Error")
            count += 1
            sent = sock.sendto(final_msg, server_address)
            time.sleep(g.next())

        sent = sock.sendto("End", server_address)
        end_time = time.time()
        print(end_time - start_time)
        print ("Per Package")
        print (10 ** 3 * args.rate)


