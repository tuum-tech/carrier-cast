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
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": [
    {
      "id": "EmTQgTBFKMNgmNeXg9KpWLmgdpbuk8XfKzp24E9skj8d",
      "status": "offline"
    }
  ]
}
```
- Get userid of self
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["userid"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "FJyFoFiRkoBiSzcvWAruEKCrF9EfxPKX41zTEAddy1vt"
}
```
- Get address of self
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["address"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "YTDzwrNXQrouMxzJfPnR7DYefpSnXScXKhRpSVt62NzmABAw4Szi"
}
```
- Create a new group
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["gnew"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "Hsk7Rhhyzmz766aAwwCqgA5xQYHoiebSWou7o24yFV3A"
}
```
- Retrieve all the groups 
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["glist"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": [
    "fLChMuc7rS2kGqrrxFVwvfzJWz9EyjLdKJLvCCQHBaR",
    "D1cfvWT39TciMfvRMzCcPkejsULyyn39q7EsYPDpDGN7",
    "Hsk7Rhhyzmz766aAwwCqgA5xQYHoiebSWou7o24yFV3A"
  ]
}
```
- Retrieve all the users in a particular group
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["gpeers fLChMuc7rS2kGqrrxFVwvfzJWz9EyjLdKJLvCCQHBaR"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": [
    "FJyFoFiRkoBiSzcvWAruEKCrF9EfxPKX41zTEAddy1vt",
    "EmTQgTBFKMNgmNeXg9KpWLmgdpbuk8XfKzp24E9skj8d",
    "6DtMUa6SQDZdWWE78u2LEZkeDqaBRZSCtESudVQakukg",
    "A9RMhbuxjA35foiR9jN4rhyeN211e5wBZDKoGiisQHPV",
    "AQAq1XqJKCSBh8MwXZ2dHRtbV5v1YJpE11xALpSHErew",
    "2zACoN7hBD6Maybgez8JikfttEG3Z7ebFyFgHQAsjk1Z"
  ]
}
```
- Remove someone from friends list
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["fremove EmTQgTBFKMNgmNeXg9KpWLmgdpbuk8XfKzp24E9skj8d"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "success"
}
```
- Invite someone to a specific group
```
curl -H 'Content-Type: application/json' -H 'Accept:application/json' --data '{"method": "send_command","params": ["ginvite FJyFoFiRkoBiSzcvWAruEKCrF9EfxPKX41zTEAddy1vt EmTQgTBFKMNgmNeXg9KpWLmgdpbuk8XfKzp24E9skj8d"],"jsonrpc": "2.0","id": 0}' http://localhost:5000
```
should print something like
```
{
  "jsonrpc": "2.0",
  "id": 0,
  "result": "success"
}
```

## Build(Only if you modify any files)
```
docker build -t tuumtech/carrier-cast .
docker push tuumtech/carrier-cast
```

## Log into the container
```
docker container exec -it carrier-cast bash
```