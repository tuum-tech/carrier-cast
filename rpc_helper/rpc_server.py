import gevent
import gevent.pywsgi
import gevent.queue
import json
import random
import string
import logging
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
	result_string = "" 
	logging.basicConfig(filename='rpc_server.log',level=logging.DEBUG,format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
	#generate a random 5 character token to send to server and 
	#use it from response to tie response to request
	letters = string.ascii_lowercase
	cmd_token = ''.join(random.choice(letters) for i in range(5))
	q = posixmq.Queue('/carrier_node_server_queue',serializer=RawSerializer)
	q.put(cmd_token.encode('ascii')+command.encode('ascii'))
	print("rpc_server: Sent command '{0}' to queue 'carrier_node_server_queue'".format(command))
	logging.info("rpc_server: Sent command '{0}' to queue 'carrier_node_server_queue'".format(command))
	q_return = posixmq.Queue('/carrier_rpc_client_queue',serializer=RawSerializer)
	while(1):
		output = ""+str(q_return.get(timeout=5).decode('ascii'))
		#print("output: "+output)
		if output[0:5]==cmd_token:
			if output[5:]!="EOS":
				result_string += output[5:]
			else:
				break
	print("rpc_server: Got response from command: {0}, Response: {1}".format(command, result_string))
	logging.info("rpc_server: Got response from command: {0}, Response: {1}".format(command, result_string))
	try:
		result = json.loads(result_string)
	except:
		result = result_string
	return result



# in the main greenlet, run our rpc_server
rpc_server.serve_forever()
