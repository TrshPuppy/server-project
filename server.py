# from flask import Flask as trsh_puppy_is_learning_python # Flas -@Gaped
# from flask import make_response

# danger_fart = trsh_puppy_is_learning_python("flask_thing") # app - @Packer

# @danger_fart.route("/", methods=["GET"])
# def hello_world():
#     return "<p>Hello, World!</p>"
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)


class Bananananananananas:  # Message - @GapedBrain
    def __init__(self, ID, mode, sock, host, port):
        self.ID = ID
        self.mode = mode
        self.suck = sock  # self.sock - @rulerlefi
        self.addr = [host, port]
        self.header_one = None
        self.header_two = None
        self.message_bytes = b""
        self.message_string = ""
        self.message_complete = False

    def _read(self):
        try:
            data_chunk = self.suck.recv(4096)
        except:
            print("except in _read try block")
            pass
        else:
            if data_chunk:
                self.message_bytes += data

    def read(self):
        if self.mode == "w":
            return

        self._read()

        if self.header_one == None and self.message_bytes >= 2:
            header = self.message_bytes
            self.process_header_one(header)

    def process_header_one(self, header):
        header_length = 2

        self.header_one = header.decode("utf-8", "replace")
        print(self.header_one)

        return


def start_socket_listen():
    message_ID = 0
    Socktopus = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket
    Socktopus.bind((HOST, PORT))
    Socktopus.listen()

    connection, address = Socktopus.accept()
    with connection:
        print(f"Connection to: {address}")
        while True:
            if connection.recv(1024):
                message = Bananananananananas(
                    message_ID, "r", Socktopus, address[0], address[1]
                )
                if message.message_complete:
                    print("message complete: " + message)
                    connection.sendall(message.message_string.encode("utf-8", "strict"))
                    Socktopus.close()
                    message_ID += 1
                    break


start_socket_listen()
"""
 message:
    properties:
        where it's from
            address
            socket
        headers
            header one: the lenght of header 2 (utf)
            header 2: the length of the message, plus the encoding?
        message:
            chunks of received data (b"")
            request
        receive_completed: (boolean)

    methods:
        a function which handles the data stream
            adds chunks to the buffer
            until message length is met

        a reading function

        a writing function
        
        process header one
            2 bytes

        process header two
            ehatever header one says

        process message/ data

        get coimplete message

        return data
 """


# Make the socket:
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Socktopus:
#     Socktopus.bind((HOST, PORT))
#     Socktopus.listen()
#     connection, address = Socktopus.accept()
#     with connection:
#         print(f"Connected by {address}")
#         while True:
#             data = connection.recv(1024)  # blocking?
#             print(data.decode("utf-8", "replace"))
#             if not data:
#                 break
#             connection.sendall(data)


"""
server:

give it socket
start the server
make socket listen for incoming requests
    when there is a request coming in:
        create the connection (with incoming address, and ID)
            send the client a message about successful connection
        keep it open (check to make sure an entire mesaage has come in)
            headers?
            decoding/encoding?
        when the message is complete, close the connection


INCORPORATE MESSAGE CLASS:
    - Id incoming messages (uniquely)
    - each new message receives a new ID
    - create new socket for ea?
        - too many sockets?
        
    - handle blocking?

"""
