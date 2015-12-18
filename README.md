Introduction
============
This game can be played over a network, local or internet. However internet play is not possible on slow connections due to lack of any latency optimizations.

Requirements
============
1) PyGame
2) RPyC

Configuration/Installation
===========================
There are three files, one server (Game.py) and two client files (Client1.py & Client2.py).
The files are configured to work on 'localhost' by default. 

If you want to play on different computers, find the following line in the client files:

`conn = rpyc.connect('localhost', 12345, config={"allow_all_attrs": True})`

and replace `localhost` with the IP Address of the server.

`python Game.py` will start the server. 
`python Clientx.py` will connect to the server and start the game.

### Game logic and physics
The game passes around a gamedata dictionary that contains all the variables related to the position of the elements. This dictionary is passed by the server to the clients and the clients use it to render the objects (using PyGame library functions). When a player gives keyboard inputs on the client side, these inputs are passed via the RPyC connection to the movepad function back at the server. The function updates the gamedata dictionary with the pad and ball's new positions and sends it back to the client. 

The physics logic of the game is fairly simple, just a bunch of `if` statements that take care of the ball and pads' movements and collision detection. This is all contained in the server file.

### Network communication
The game has a client-server model. The client runs a `while 1:` loop which takes keyboard inputs. The server runs an RPyC server that listens for connections. 

The server has a `PongGame` class which extends the `rpyc.Service` class. This enables it to expose functions that can be invoked by clients remotely. Once the client establishes a connection with the server, the PongGame class's exposed methods are at its disposal. In our case, it is the `exposed_movepad` function.

###Possible improvements
The game can be improved greatly by adding the following features:

1) Game loop and listening server on the server side: This is an absolutely essential requirement.  Right now, the server  runs a blocking server so there is no way to run a game loop on the server side. If we can run the server in the background or use some asynchronous logic, then we can have the game loop in the server. This will solve the issue of the ball moving only when a player makes a move.

2) Game physics fine tuning: I have not paid much attention to the if statements of the ball and pad movement logic because of the limitation of the ball moving only when the player moves. Once we can run the game loop on the server, the game will become much easier to play and then these changes will be easy to make.
