import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 5001  # The port used by the server


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
            print(f"try statement {data_chunk}")
        except:
            print("except in _read try block")
            return f""
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

        if self.header_one != None:
            self._read()

        if self.header_one != None:
            next_chunk = self.suck.recv(2)
            print(f"next chunk ({next_chunk}) and length {len(next_chunk)}")

    def process_header_one(self, header):
        # this header should tell us how long the next header is
        # header_length = 2
        self.header_one = header.decode("utf-8", "replace")
        print(f"length of tiddies {len(self.header_one)}")

        return


# these headers need IDs eventually
header_one_data = 4
header_one = chr(header_one_data) + chr(0)

header_two_data = 6

illillllllillllllllll = chr(header_two_data)  # @zoogod5000 "header_two"
for byte in range(header_one_data - 1):
    illillllllillllllllll += chr(0)

cheese_data = "tiddie"  # @mezmiro "message"
cheese = cheese_data


entire_message = header_one + illillllllillllllllll + cheese
print(entire_message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(entire_message.encode("utf-8", "strict"))
    s.sendall(entire_message.encode("utf-8", "strict"))
    data = s.recv(1024)

print(f"Received {data!r}")


"""
fake message:

4 : 6 : tiddies

"46tiddies"


"""
