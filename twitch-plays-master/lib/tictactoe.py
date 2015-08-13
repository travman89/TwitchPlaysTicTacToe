# created by Travis Davisson
import sys

def calculate_win_condition(game_tracker):
#Checks all possible win conditions for a winning row
	if game_tracker[0]==game_tracker[1] and game_tracker[0]==game_tracker[2] and game_tracker[0]!=0:
#		print "win condition 1"
		return True
	elif game_tracker[0]==game_tracker[3] and game_tracker[0]==game_tracker[6] and game_tracker[0]!=0:
#		print "win condition 2"
		return True
	elif game_tracker[0]==game_tracker[4] and game_tracker[0]==game_tracker[8] and game_tracker[0]!=0:
#		print "win condition 3"
		return True
	elif game_tracker[1]==game_tracker[4] and game_tracker[1]==game_tracker[7] and game_tracker[1]!=0:
#		print "win condition 4"
		return True
	elif game_tracker[2]==game_tracker[5] and game_tracker[2]==game_tracker[8] and game_tracker[2]!=0:
#		print "win condition 5"
		return True
	elif game_tracker[3]==game_tracker[4] and game_tracker[3]==game_tracker[5] and game_tracker[3]!=0:
#		print "win condition 6"
		return True
	elif game_tracker[6]==game_tracker[7] and game_tracker[6]==game_tracker[8] and game_tracker[6]!=0:
#		print "win condition 7"
		return True
	elif game_tracker[6]==game_tracker[4] and game_tracker[6]==game_tracker[2] and game_tracker[6]!=0:
#		print "win condition 8"
		return True
	else:
		return False
		

def check_cats_game(game_tracker):
#checks if the game is winnable
	moves = 0
	for move in game_tracker:
		if move != 0:
			moves+=1
	if moves == 9: 
		return calculate_win_condition(game_tracker)
	else:
		return False
		
			