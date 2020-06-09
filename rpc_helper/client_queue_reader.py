from ipcqueue import posixmq
from ipcqueue.serializers import RawSerializer

q_return = posixmq.Queue('/carrier_node_client_queue',serializer=RawSerializer)
while (1):
	print("waiting")
	output = ""+str(q_return.get().decode('ascii'))
	print("return %s" % output)

