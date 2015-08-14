import time

from config.config import config
from lib.irc import Irc
from lib.game import Game
from lib.misc import pbutton
from lib.tictactoe import *
import pygame, sys
from pygame.locals import *
from pygame.mixer import *
from random import choice
pygame.init()

class Bot:

    def __init__(self):
        self.config = config
        self.irc = Irc(config)
        self.game = Game()
        self.message_buffer = []
        self.scrolling_chat = []
        self.chat_buffer = []
        self.game_tracker = [0,0,0,0,0,0,0,0,0]
        self.windowSurface = pygame.display.set_mode((1300,800), 0, 32)
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.start = time.clock()
        self.game_timer = 0
        self.old_time = 0;
        self.xwins = 0
        self.owins = 0
        self.cats_games = 0
        self.games = 0
        self.who_starts = 0
        self.whos_move = 0
        self.suspend = 0
        self.winner = False
        self.is_cats = False
        self.music = pygame.mixer.Sound('music_loop.wav')
        self.basicFont = pygame.font.SysFont(None, 36)
	
    def reset_message_buffer(self):
        self.message_buffer = []

    def draw_x1(self):
        pygame.draw.line(self.windowSurface, self.WHITE, (180,180), (266,266), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (180,266), (266,180), 4)
   
    def draw_x2(self):
        pygame.draw.line(self.windowSurface, self.WHITE, (334,180), (420,266), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (334,266), (420,180), 4)
		
    def draw_x3(self):
        pygame.draw.line(self.windowSurface, self.WHITE, (488,180), (574,266), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (488,266), (574,180), 4)
		
    def draw_x4(self):
        pygame.draw.line(self.windowSurface, self.WHITE, (180,334), (266,420), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (180,420), (266,334), 4)
		
    def draw_x5(self):    
        pygame.draw.line(self.windowSurface, self.WHITE, (334,334), (420,420), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (334,420), (420,334), 4)
		
    def draw_x6(self):
        pygame.draw.line(self.windowSurface, self.WHITE, (488,334), (574,420), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (488,420), (574,334), 4)
		
    def draw_x7(self):
        pygame.draw.line(self.windowSurface, self.WHITE, (180,488), (266,574), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (180,574), (266,488), 4)
		
    def draw_x8(self):
        pygame.draw.line(self.windowSurface, self.WHITE, (334,488), (420,574), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (334,574), (420,488), 4)
		
    def draw_x9(self):
        pygame.draw.line(self.windowSurface, self.WHITE, (488,488), (574,574), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (488,574), (574,488), 4)
		
    def draw_o1(self):
        pygame.draw.circle(self.windowSurface, self.WHITE,(223,223), 43, 4)
   
    def draw_o2(self):
        pygame.draw.circle(self.windowSurface, self.WHITE,(377,223), 43, 4)
		
    def draw_o3(self):
        pygame.draw.circle(self.windowSurface, self.WHITE,(531,223), 43, 4)
		
    def draw_o4(self):
        pygame.draw.circle(self.windowSurface, self.WHITE,(223,377), 43, 4)
		
    def draw_o5(self):
        pygame.draw.circle(self.windowSurface, self.WHITE,(377,377), 43, 4)
		
    def draw_o6(self):
        pygame.draw.circle(self.windowSurface, self.WHITE,(531,377), 43, 4)
		
    def draw_o7(self):
        pygame.draw.circle(self.windowSurface, self.WHITE,(223,531), 43, 4)
		
    def draw_o8(self):
        pygame.draw.circle(self.windowSurface, self.WHITE,(377,531), 43, 4)
		
    def draw_o9(self):
        pygame.draw.circle(self.windowSurface, self.WHITE,(531,531), 43, 4)
		
#draws the tic tac toe board
    def draw_board(self):
        self.windowSurface.fill(self.BLACK)
        pygame.draw.line(self.windowSurface, self.WHITE, (300,150), (300,600), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (446,150), (446,600), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (150,296), (600,296), 4)
        pygame.draw.line(self.windowSurface, self.WHITE, (150,450), (600,450), 4)
 
    def draw_scores(self):
        xtext = self.basicFont.render("X WINS: %s" % str(self.xwins), True, self.WHITE, self.BLACK)
        xtextRect = xtext.get_rect()
        xtextRect = xtextRect.move(10,10)
        otext = self.basicFont.render("O WINS: %s" % str(self.owins), True, self.WHITE, self.BLACK)
        otextRect = otext.get_rect()
        otextRect = otextRect.move(250,10)
        catstext = self.basicFont.render("CATS GAMES: %s" % str(self.cats_games), True, self.WHITE, self.BLACK)
        catstextRect = catstext.get_rect()
        catstextRect = catstextRect.move(500,10)
        self.windowSurface.blit(xtext, xtextRect)
        self.windowSurface.blit(otext, otextRect)
        self.windowSurface.blit(catstext, catstextRect)
#draws the symbols 
    def draw_symbols(self):
        if self.game_tracker[0] == 1:
            self.draw_o1()
        if self.game_tracker[1] == 1:
            self.draw_o2()
        if self.game_tracker[2] == 1:
            self.draw_o3()
        if self.game_tracker[3] == 1:
            self.draw_o4()
        if self.game_tracker[4] == 1:
            self.draw_o5()
        if self.game_tracker[5] == 1:
            self.draw_o6()
        if self.game_tracker[6] == 1:
            self.draw_o7()
        if self.game_tracker[7] == 1:
            self.draw_o8()
        if self.game_tracker[8] == 1:
            self.draw_o9()
        if self.game_tracker[0] == 2:
            self.draw_x1()
        if self.game_tracker[1] == 2:
            self.draw_x2()
        if self.game_tracker[2] == 2:
            self.draw_x3()
        if self.game_tracker[3] == 2:
            self.draw_x4()
        if self.game_tracker[4] == 2:
            self.draw_x5()
        if self.game_tracker[5] == 2:
            self.draw_x6()
        if self.game_tracker[6] == 2:
            self.draw_x7()
        if self.game_tracker[7] == 2:
            self.draw_x8()
        if self.game_tracker[8] == 2:
            self.draw_x9()

    def get_scrolling_chat(self):
        if len(self.chat_buffer) > 0:
            if (len(self.scrolling_chat) + len(self.chat_buffer)) > 25:
                if len(self.chat_buffer) > 25:
                    self.scrolling_chat = self.chat_buffer[(len(self.chat_buffer)-25):]
                else:
                    del self.scrolling_chat[:len(self.chat_buffer)]
                    for item in self.chat_buffer:
                        self.scrolling_chat.append(item)
            else:
                for item in self.chat_buffer:
                    self.scrolling_chat.append(item)
        self.chat_buffer = []
            
    def draw_scrolling_chat(self):	
        counter = 0
        text = self.basicFont.render("CHAT COMMANDS", True, self.WHITE, self.BLACK)
        textRect = text.get_rect()
        textRect = textRect.move(870,10)
        self.windowSurface.blit(text, textRect)
        for item in self.scrolling_chat:
            text = self.basicFont.render(str(item), True, self.WHITE, self.BLACK)
            textRect = text.get_rect()
            textRect = textRect.move(870,(60+(25*counter)))
            self.windowSurface.blit(text, textRect)
            counter+=1
			
    def draw_game(self):
        self.draw_board()
        self.draw_symbols()
        self.draw_scores()
        self.draw_scrolling_chat()
        pygame.display.update()
	
    def reset_game(self):
        self.game_tracker = [0,0,0,0,0,0,0,0,0]
        self.game_timer = time.clock()
        self.old_time = 0
        self.suspend = 0
        self.who_starts += 1
        self.whos_move = self.who_starts%2
        self.winner = False
        self.is_cats = False
		
    def choose_random_move(self):
        templist = []
        counter = 0
        for move in self.game_tracker:
            if move == 0:
                templist.append(counter)
            counter+=1
        return choice(templist)

    def get_valid_moves(self):
        templist = []
        counter = 0
        for move in self.game_tracker:
            if move == 0:
                templist.append(counter+1)
            counter+=1
        return templist
		
        #TODO fix allows user selected move to overwrite filled in spaces.
    def choose_user_move(self):       
        valid_moves = self.get_valid_moves()
        print valid_moves
        templist = [0,0,0,0,0,0,0,0,0]
        for item in self.message_buffer:
            if int(item) in valid_moves:
                templist[int(item)-1]+=1
#        print templist
        max_votes = 0
        for item in templist:
            if item > max_votes:
                max_votes = item
#        print "max votes = %s" % max_votes
        moves_choices = []
        counter = 0
        for item in templist:
            if item == max_votes and max_votes>0:
                moves_choices.append(counter)
            counter+=1
        self.reset_message_buffer()
        print moves_choices
        if len(moves_choices) == 0:		
            return self.choose_random_move()
        else:
            return choice(moves_choices)
		
    def choose_move(self):
        if len(self.message_buffer) == 0:
            random_move = self.choose_random_move()
            print("random move")
            print random_move
            return random_move
        else:
            user_move = self.choose_user_move()
       #     print user_move
            return user_move
			
    def make_move(self):
        if self.winner == True or self.is_cats == True:
            self.games+=1
            self.reset_game()
        elif self.winner == False:
            count = 0
            for move in self.game_tracker:
                if move == 0:
                    count+=1
                    break
            if count > 0:
                self.game_tracker[self.choose_move()]=self.whos_move+1
                if calculate_win_condition(self.game_tracker):
                    self.winner = True
                    if self.whos_move == 0:
                        self.owins+=1
                    else:
                        self.xwins+=1
            elif calculate_win_condition(self.game_tracker):
                self.winner = True
                if self.whos_move == 0:
                    self.owins+=1
                else:
                    self.xwins+=1
            else:
                self.is_cats = True
                self.cats_games+=1
				
    def alternate_turn(self):
        if self.whos_move == 0:
            self.whos_move = 1
        else:
            self.whos_move = 0
    def run(self):
		# created by Aidan Thomson
        #throttle_timers = {button:0 for button in config['throttled_buttons'].keys()}
        #get new messages from chat. Store valid messages only in the message buffer list 
		#after 5-10 seconds calculate the move that was chosen. If no move was chosen automatically choose an open one.
		#update the board.
		#calculate an end game condition
		#
        self.reset_game()
        #self.music.play(-1)

        while True:
           # self.draw_game()
            timer = time.clock() - self.game_timer
            if((timer-self.old_time)>.90):
                self.old_time = timer
                timer = int(timer)
 #
                self.draw_game()
                # every 10 seconds make a move and check for a win
                if timer > 0 and timer%3 == 0:
                    self.make_move()
                    self.alternate_turn()
				
            new_messages = None
            new_messages = self.irc.recv_messages(1024)   
            if new_messages != None: 
                for message in new_messages: 		
                    button = message['message'].lower()
                    username = message['username'].lower()
               #     print username + " " + button
                    if self.game.is_valid_button(button): 
                #        print button
                        self.message_buffer.append(button)
                        self.chat_buffer.append(str(username + ': ' + button))
                self.get_scrolling_chat()
#                self.reset_message_buffer()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
              #  pbutton(self.message_buffer)
              #  self.game.push_button(button)

