
import socket
import json

host = 'localhost' 
port = 5204
backlog = 5 
size = 2048 


class Server():

    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind((host,port)) 
        s.listen(backlog)

        print("Waiting for client...")
        self.client, address = s.accept() 
        print ("Client connected")
        
    def read(self):
        byte_data = self.client.recv(size)
        try:
            str_data = byte_data.decode('utf8')
            json_data = json.loads(str_data)
            return json_data
        except Exception as e:
            pass
            #print("Error in server read: ", e)
            #print('json_data: ', json_data)


    def write(self, msg):
        msg = json.dumps(msg).encode('utf-8')
        self.client.send(msg)

    def close(self):
        self.s.close()


        #client.close()