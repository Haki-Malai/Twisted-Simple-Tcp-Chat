from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol

FORMAT = 'utf-8'

class Client(Protocol):
    def __init__(self):
        reactor.callInThread(self.send_data)
        
    def dataReceived(self, data):
        data = data.decode(FORMAT)
        print(data)

    def send_data(self):
        while True:
            self.transport.write(input(":::").encode(FORMAT))

class ClientFactory(Factory):
    def buildProtocol(self, addr):
        return Client()
    
if __name__ == '__main__':
    endpoint = TCP4ClientEndpoint(reactor, "localhost", 2000)
    endpoint.connect(ClientFactory())
    reactor.run()
