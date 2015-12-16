# networkpong

Welcome to the worst network game in the world. This game is unplayable because of latency but if you still want to play it, please download a client.py file and inform me.
I will start the game on the server and we can then play network pong!

The game requires two python libraries, please install them before attempting to play:
1) PyGame
2) RPyC

If you want to enjoy this game on a 'localhost', please replace the ip of the server in the Game.py and Clientx.py files with 'localhost' and voila, latency gone!

However, the ball moves only when a player moves, because I haven't figured out how to run a game loop and a server at the same time. So at any time, either the server will block the process or the "while 1" game loop will. Suggestions on how to overcome this are welcome.
