# from flask import Flask as trsh_puppy_is_learning_python # Flas -@Gaped
# from flask import make_response

# danger_fart = trsh_puppy_is_learning_python("flask_thing") # app - @Packer

# @danger_fart.route("/", methods=["GET"])
# def hello_world():
#     return "<p>Hello, World!</p>"
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 5001  # Port to listen on (non-privileged ports are > 1023)


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

    def _read(self, bytes_to_read):
        try:
            data_chunk = self.suck.recv(bytes_to_read)
        except:
            print("except in _read try block")
            return
        else:
            if data_chunk:
                self.message_bytes += data_chunk
            return data_chunk

    def read(self):
        if self.mode == "w":
            return

        header_one = self._read(2)
        if header_one:
            self.process_header_one(header_one)

        header_two = None
        if self.header_one != None:
            header_2_length = self.header_one
            header_two = self._read(header_2_length)

        if header_two:
            self.process_header_two(header_two)

        data_received = None
        if self.header_two != None:
            data_length = self.header_two
            data_received = self._read(data_length)

        if data_received:
            self.process_data_received(data_received)

    def process_header_one(self, header):
        # this header should tell us how long the next header is
        self.header_one = header[0]
        return

    def process_header_two(self, header):
        # this header should tell us how long the data is
        self.header_two = header[0]
        return

    def process_data_received(self, data):
        self.message_string = data.decode("utf-8")
        if len(self.message_string) == self.header_two:
            self.message_complete = True
        else:
            # do something here about checking for more data
            print("self.message_string length != entire predicted length")
            pass
        return


def start_socket_listen():
    message_ID = 0
    Socktopus = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket
    Socktopus.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Socktopus.bind((HOST, PORT))
    Socktopus.listen()

    connection, address = Socktopus.accept()
    with connection:
        print(f"Connection to: {address}")
        while True:
            message = Bananananananananas(
                message_ID, "r", connection, address[0], address[1]
            )
            message.read()
            if message.message_complete:
                print("Data received in full.")
                connection.sendall(message.message_string.encode("utf-8", "strict"))
                Socktopus.close()
                message_ID += 1
                break
            if KeyboardInterrupt():
                Socktopus.close()
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
