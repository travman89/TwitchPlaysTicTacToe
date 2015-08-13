# TwitchPlaysTicTacToe

This code is a twitch plays clone with a tic tac toe game included.  The original code to grab the twitch chat was written by
Aidan Thmopson and can be found [here](https://github.com/aidraj/twitch-plays).

# Installation
Follow the installation instructions [here](https://github.com/aidraj/twitch-plays#installation).

You will also need to install [pygame](http://www.pygame.org/download.shtml) in order for the tic tac toe game to run.

Once everything is installed simply run the serve.py script.

# Gameplay
The game logic takes all of the twitch chat valid inputs within the time limit. It totals up the valid votes for the open positions
and selects the space that was voted for in chat.  If no votes are cast via chat then the game will select an open space and fill
in the next move. Valid chat commands will be shown on the game screen.

![alt tag](http://i.imgur.com/JJ156Ek.png)
