# Carrier Cast

Carrier Cast is a program that runs on a linux system and creates an ElastOS carrier node.  Carrier nodes support all peer-to-peer communications in the ElastOS ecosystem.  By using Carrier Cst you will be able to host an always-on node to support communications that support many types of applications. 

Carrier Cast provides an RPC server that accepts and executes all elashell commands.  


## Run
```
./run.sh
```

## Sample RPC
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["friends"],"jsonrpc": "2.0","id": 0}'  http://127.0.0.1:5000/  
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["gnew"],"jsonrpc": "2.0","id": 0}'  http://127.0.0.1:5000/  
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["glist"],"jsonrpc": "2.0","id": 0}'  http://127.0.0.1:5000/ 
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["gpeers B9E9HJKpAXs9w5Sa9CaMCqKXDpnq2X836no7af7QYyZQ"],"jsonrpc": "2.0","id": 0}'  http://127.0.0.1:5000/
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["fremove 9PPuqkVrXx9TQH5pGsh1mwgMTTjwDaw7SehpUbLNH8VJ"],"jsonrpc": "2.0","id": 0}'  http://127.0.0.1:5000/
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["ginvite B9E9HJKpAXs9w5Sa9CaMCqKXDpnq2X836no7af7QYyZQ 9PPuqkVrXx9TQH5pGsh1mwgMTTjwDaw7SehpUbLNH8VJ"],"jsonrpc": "2.0","id": 0}'  http://127.0.0.1:5000/
```

## Build(Only if you modify any files)
```
docker build -t tuumtech/carrier-cast .
docker push tuumtech/carrier-cast
```