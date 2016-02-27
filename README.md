# 2048
2048 game, played via CLI on Python 3 IDLE

1. Save cli2048.py in a directory of your choice.

2. Open Python IDLE and enter the following:

    import os  
    os.chdir(r'c:\location\of\cli2048py')  # please edit string to the correct path  
    from cli2048 import Game  
    g = Game()  

3. A game has begun! View the board with:

    g.show()  

4. Play 2048 using the commands below. Tip: Alt+P cycles through previously entered commands.

    g.up()  
    g.down()  
    g.left()  
    g.right()  

Enjoy.

## Work in progress:

- The default grid is 4x4. To play on a nxn grid, initialise the game with:

	g = Game(n)

- You can turn debug mode on and off, which displays number spawn locations and whether any numbers have moved.

	g.debug = True
	g.debug = False #default

