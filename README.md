# Carrier Cast

Carrier Cast is a program that runs on a linux system and creates an ElastOS carrier node.  Carrier nodes support all peer-to-peer communications in the ElastOS ecosystem.  By using Carrier Cst you will be able to host an always-on node to support communications that support many types of applications. 

Carrier Cast provides an RPC server that accepts and executes all elashell commands.  


## Run
```
./run.sh
```

## How to interact with RPC endpoints
- Get friends list and their status
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["friends"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
``` 
should print something like
```

```
- Get userid of self
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["userid"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "id": 0,
  "result": "7nkEktqycBWWhQipvbrGXaUKxY3Yz4WwgjAjZpoRNKru\u000",
  "jsonrpc": "2.0"
}

```
- Create a new group
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["gnew"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "id": 0,
  "result": "group:2i2kyu27AkhZ1YUt1anPRVLro18R7hUQGVJKfmUAu1S2,\u0000",
  "jsonrpc": "2.0"
}
```
- Retrieve all the groups 
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["glist"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "id": 0,
  "result": "groups:[2i2kyu27AkhZ1YUt1anPRVLro18R7hUQGVJKfmUAu1S2,2yrbATvSvnBrNVoDzvrBot464ivuQ5CCQS2mfq5NxQYt,]\u0000",
  "jsonrpc": "2.0"
}
```
- Retrieve all the users in a particular group
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["gpeers 2i2kyu27AkhZ1YUt1anPRVLro18R7hUQGVJKfmUAu1S2"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "id": 0,
  "result": "peers:[7nkEktqycBWWhQipvbrGXaUKxY3Yz4WwgjAjZpoRNKru,]\u0000",
  "jsonrpc": "2.0"
}
```
- Remove someone from friends list
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["fremove EmTQgTBFKMNgmNeXg9KpWLmgdpbuk8XfKzp24E9skj8d"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```

```
- Invite someone to a specific group
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["ginvite 2i2kyu27AkhZ1YUt1anPRVLro18R7hUQGVJKfmUAu1S2 EmTQgTBFKMNgmNeXg9KpWLmgdpbuk8XfKzp24E9skj8d"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```

```

## Build(Only if you modify any files)
```
docker build -t tuumtech/carrier-cast .
docker push tuumtech/carrier-cast
```