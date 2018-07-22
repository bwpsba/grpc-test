Setup gRPC
===========
`make`


Run server
===========
`python server.py`

-or-

Run with some debugging:
`GRPC_VERBOSITY=DEBUG GRPC_TRACE=executor,timer,channel,inproc,connectivity_state,server_channel python server.py`


Run client that uses default sizes
===========
`python client.py 100`  # ask for a 100-byte string to be returned

Run client asking for more data than can be handled by default:

`python client.py $(( 1024 * 1024 * 4 ))`  # expect to see error here


Run client that increases limits it can handle
===========

`python client_accept_large.py $(( 1024 * 1024 * 4 ))`  # success


Diff
===========
```
$ diff client.py client_accept_large.py
7c7,9
< channel = grpc.insecure_channel('localhost:53051')
---
> options = [('grpc.max_send_message_length', 1024 * 1024 * 20), ('grpc.max_receive_message_length', 1024 * 1024 * 20)]
>
> channel = grpc.insecure_channel('localhost:53051', options=options)
```
