from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

FORMAT = 'utf-8'
class Server(Protocol):
    def __init__(self, users):
        self.users = users
    
    def connectionMade(self):
        self.users.append(self)
        self.transport.write("Hello from server.".encode(FORMAT))
        
    def dataReceived(self, data):
        for user in self.users:
            if user != self:
                user.transport.write(data)
        
class ServerFactory(Factory):
    def __init__(self):
        self.users = []
        
    def buildProtocol(self, addr):
        return Server(self.users)

if __name__ == '__main__':
    # 8007 is the port you want to run under. Choose something >1024
    endpoint = TCP4ServerEndpoint(reactor, 2000  )
    endpoint.listen(ServerFactory())
    reactor.run()
