import socket

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 10000))
 
    while True:
        try:
            command =  s.recv(1024)

            if command in "0":
                print "Password Valid"
                break
            elif command in "1":
                print "Password Invalid"
                break
            else:
                print command
                password = raw_input("\nPassword: ")
                s.send(password)
        except Exception as e:
            break
        
if __name__ == '__main__':
    connect()