import socket

IP_ADDRESS = "localhost"

PORT = 8080

cs = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
cs.connect((IP_ADDRESS, PORT))

msg_to_server = "Hello Server, I want to play with you"
cs.sendto(msg_to_server.encode("ascii"), (IP_ADDRESS, PORT))
message, address = cs.recvfrom(1024)
message = message.decode()
print(message)

while True:
    clientGuess = input("Enter A Prime Number Between 1 and 50: ")
    clientGuess = clientGuess.lower().strip()
    cs.sendto(clientGuess.encode("ascii"), address)
    if clientGuess == "over":
        print("Thank You Playing, Game Ended, Here Are The Summary Stats: ")
        message, _ = cs.recvfrom(1024)
        message = message.decode()
        print(message)
        cs.close()
        break
    message, address = cs.recvfrom(1024)
    higher = message.decode()
    print(higher)
    message, address = cs.recvfrom(1024)
    stats = message.decode()
    print(stats)