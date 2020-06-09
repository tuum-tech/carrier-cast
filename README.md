# Carrier Cast

Carrier Cast is a program that runs on a linux system and creates an ElastOS carrier node.  Carrier nodes support all peer-to-peer communications in the ElastOS ecosystem.  By using Carrier Cst you will be able to host an always-on node to support communications that support many types of applications. 

Carrier Cast provides an RPC server that accepts and executes all elashell commands.  


## Build 
```
docker build -t tuum-tech/carrier-cast .
```

## Run
```
./run.sh
```

## Sample RPC
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["friends"],"jsonrpc": "2.0","id": 0}'  http://127.0.0.1:5000
```