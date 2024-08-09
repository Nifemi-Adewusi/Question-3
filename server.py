import socket
import random

tries = 0
clientWins = 0
serverWins = 0
draws = 0
cashPrice = 0

def checkPrimeNumber(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generatePrimeNumbers(limit):
    primeNumbers = []
    for num in range(1, limit + 1):
        if checkPrimeNumber(num):
            primeNumbers.append(num)
    return primeNumbers

def checkGuessValidity(clientGuess, serverGuess):
    global clientWins, serverWins, draws, tries, cashPrice
    output = ""
    if serverGuess > clientGuess:
        tries += 1
        serverWins += 1
        output = "No it is a little higher than that, kindly try again"
    elif serverGuess < clientGuess:
        tries += 1
        clientWins += 1
        output = "Sorry My Client, it is a little lower than that, kindly try again"
    elif clientGuess == serverGuess:
        tries+=1
        cashPrice+=200000
        draws+=1
        output = "Congratulations!!! You Won a cash price of 20000"
    return output

def showStats():
    return f"Game {tries}: Client Guessed The Same Prime Number As The Server {draws} times, Server Guessed Higher Than The  Client {serverWins} times, Client's Guess Exceeds Server Guess {clientWins} times and there has been a total cash price of {cashPrice} so far"


IP_ADDRESS = "localhost"

PORT = 8080

ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

ss.bind((IP_ADDRESS, PORT))
message, address = ss.recvfrom(1024)
message = message.decode()
print(message)
msg_to_client = "Kindly Send A Prime Number"
ss.sendto(msg_to_client.encode("ascii"), address)

primeNumbers = generatePrimeNumbers(50)
randomIndex = random.randint(1, len(primeNumbers)-1)
serverGuess = primeNumbers[randomIndex]
print(serverGuess)
while True:
   message, address = ss.recvfrom(1024)
   clientGuess = message.decode()
   if clientGuess == "over":
       stats = showStats()
       ss.sendto(stats.encode("ascii"), address)
       ss.close()
       break
   clientGuess = int(clientGuess)
   higher = checkGuessValidity(clientGuess, serverGuess)
   stats = showStats()
   ss.sendto(higher.encode("ascii"), address)
   ss.sendto(stats.encode("ascii"), address)


