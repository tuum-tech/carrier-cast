# Carrier Cast

Carrier Cast is a program that runs on a linux system and creates an ElastOS carrier node.  Carrier nodes support all peer-to-peer communications in the ElastOS ecosystem.  By using Carrier Cst you will be able to host an always-on node to support communications that support many types of applications. 

Carrier Cast provides an RPC server that accepts and executes all elashell commands.  


## Build 
```
docker build -t tuum-tech/carrier_node .
```

## Run
- Stop previously opened docker containers
```
docker container stop carrier-node || true && docker container rm -f carrier-node || true
```
- Run the container 
```
docker run -it --name carrier-node -p 5000:5000 tuum-tech/carrier_node:latest
# nohup /Elastos.NET.Carrier.Native.SDK/build/linux/apps/shell/elashell &
```
- Open a second terminal and run the rpc server
```
docker container exec -it carrier-node python3 /rpc_server.py
```
- Open a third terminal and run the queue reader
```
docker container exec -it carrier-node python3 /client_queue_reader.py
```

## Sample RPC
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["friends"],"jsonrpc": "2.0","id": 0}'  http://127.0.0.1:5000
```