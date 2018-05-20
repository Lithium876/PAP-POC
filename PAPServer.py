import socket, hashlib
 
passwordHash= #create a MD5 hashed version of any password you wisH. Use the hashit function for this#

def hashit(password):
	'''
	Returns a hashed version of a password
	'''
	result = hashlib.md5(password.encode())
	return result.hexdigest()

def connect(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    s.bind((ip, int(port)))                           
    s.listen(1)          

    print '[+] Listening for incoming TCP connection on port',port
    conn, addr = s.accept()  

    print '[+] We got a connection from: ', addr
    conn.send("Server Received Connection")

    res= conn.recv(1024*1024)

    print "Received: ", hashit(res)

    if passwordHash in str(hashit(res)):
    	print "Client Authenticated"
    	conn.send(str(0))
    else:
        print "Client not Valid"
        conn.send(str(1)) 

if __name__ == '__main__':
    connect("localhost", 10000)
