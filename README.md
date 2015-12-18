# networkpong

Welcome to network pong! 

INTRODUCTION
============
This game can be played over a network. Local or internet, however internet play is not possible on slow connections due to lack of any latency optimizations.

REQUIREMENTS
============
1) PyGame
2) RPyC

DISCLAIMER
==========
The ball moves only when a player moves, because I haven't figured out how to run a game loop and a server at the same time. So at any time, either the rpyc "server" will block the process or the "while 1" game loop will. Suggestions on how to overcome this are welcome.
