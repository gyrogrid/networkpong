# networkpong

Welcome to network pong! 

This game can be played over any network including the internet. If you want to play it, please download a client.py file and inform me.
I will start the game on the server and we can then play!

Two python libraries are required, please install them before attempting to play:
1) PyGame
2) RPyC

However, the game isn't perfect yet. The ball moves only when a player moves, because I haven't figured out how to run a game loop and a server at the same time. So at any time, either the rpyc "server" will block the process or the "while 1" game loop will. Suggestions on how to overcome this are welcome.
