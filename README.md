# networkpong

Welcome to network pong! 

Introduction
============
This game can be played over a network, local or internet. However internet play is not possible on slow connections due to lack of any latency optimizations.

Requirements
============
1) PyGame
2) RPyC

Configuration/Installation
===========================
There are three files, one Server.py and two client files (Client1.py & Client2.py).
The files are configured to work on 'localhost' by default. 

If you want to play on different computers, find the following line in the client files:

`conn = rpyc.connect('localhost', 12345, config={"allow_all_attrs": True})`

and replace `localhost` with the IP Address of the server.


Gameplay
==========
The ball moves only when a player moves, because I haven't figured out how to run a game loop and a server at the same time. So at any time, either the rpyc "server" will block the process or the "while 1" game loop will. Suggestions on how to overcome this are welcome.
