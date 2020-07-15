from ipcqueue import posixmq
from ipcqueue.serializers import RawSerializer

posixmq.unlink('/carrier_rpc_client_queue')
posixmq.unlink('/carrier_node_client_queue')


