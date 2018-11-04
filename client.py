from autobahn.twisted.wamp import Application
from autobahn.twisted.util import sleep
from autobahn.wamp.exception import ApplicationError
#from twisted.internet.defer import returnValue

app = Application(u'com.app')
continueLoop = True

@app.register(u'com.app.hello')
def sayhello():
    return "Hello, World"

@app.register(u'com.app.ping')
def onping(msg):
    return "{}".format(msg)

@app.signal('ondisconnect')
def ondisconnect():
    continueLoop = False

@app.signal('onjoined')
def onjoined():
    print("realm1 joined!")
    while continueLoop:
        app.session.publish('com.app.ping', 'ping')
        sleep(5)

if __name__ == "__main__":
    try:
        app.run(url=u"ws://0.0.0.0:8080/ws")
    except ApplicationError as e:
        raise(e)
    



