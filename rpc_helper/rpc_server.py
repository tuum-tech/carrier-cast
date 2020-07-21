import gevent
import gevent.pywsgi
import gevent.queue
import json
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
from tinyrpc.transports.wsgi import WsgiServerTransport
from tinyrpc.server.gevent import RPCServerGreenlets
from tinyrpc.dispatch import RPCDispatcher
from ipcqueue import posixmq
from ipcqueue.serializers import RawSerializer


dispatcher = RPCDispatcher()
transport = WsgiServerTransport(queue_class=gevent.queue.Queue)

# start wsgi server as a background-greenlet
wsgi_server = gevent.pywsgi.WSGIServer(('0.0.0.0', 5000), transport.handle)
gevent.spawn(wsgi_server.serve_forever)

print("rpc_server: Initializing RPC server")
rpc_server = RPCServerGreenlets(transport, JSONRPCProtocol(), dispatcher)
#rpc_server = JSONRPCProtocol()

@dispatcher.public
def send_command(command):
	print("rpc_server: Executing command: {0}".format(command))
	longstring = "" 
	q = posixmq.Queue('/carrier_node_server_queue',serializer=RawSerializer)
	q.put(command.encode('ascii'))
	q_return = posixmq.Queue('/carrier_rpc_client_queue',serializer=RawSerializer)
	while(1):
		output = ""+str(q_return.get().decode('ascii'))
		if output!="EOS":
			longstring+=output
		else:
			break
	print("rpc_server: Got response from command: {0}, Response: {1}".format(command, longstring))
	return longstring



# in the main greenlet, run our rpc_server
rpc_server.serve_forever()
