import gevent
import gevent.pywsgi
import gevent.queue
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.wsgi import WsgiServerTransport
from tinyrpc.server.gevent import RPCServerGreenlets
from tinyrpc.dispatch import RPCDispatcher
from ipcqueue import posixmq
from ipcqueue.serializers import RawSerializer


dispatcher = RPCDispatcher()
transport = WsgiServerTransport(queue_class=gevent.queue.Queue)

# start wsgi server as a background-greenlet
wsgi_server = gevent.pywsgi.WSGIServer(('127.0.0.1', 5000), transport.handle)
gevent.spawn(wsgi_server.serve_forever)

rpc_server = RPCServerGreenlets(transport, JSONRPCProtocol(), dispatcher)

@dispatcher.public
def send_command(s):
	q = posixmq.Queue('/sp-example-server',serializer=RawSerializer)
	q.put(s.encode('ascii'))
	return "command sent"

# in the main greenlet, run our rpc_server
rpc_server.serve_forever()
