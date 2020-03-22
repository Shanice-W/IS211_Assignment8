#!/usr/bin/env python
# coding: utf-8

# In[136]:


import random
import argparse
import sys
import time


# In[137]:


parser = argparse.ArgumentParser()
parser.add_argument('--player1', help='human or computer')
parser.add_argument('--player2', help='human or computer')
parser.add_argument('--timed', help='60sec timer, yes or no')
args = parser.parse_args()


# In[ ]:


class Dice(object):
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


# In[ ]:


class Player(object):
    def __init__(self):
        self.score = 0
        self.name = 'Player'

    def addToScore(self, amount):
        self.score += amount

    def ask(self):
        pass


# In[138]:


class Computer(Player):
    def __init__(self):
        super(Computer, self).__init__()
        self.name = 'Computer'

    def ask(self, turnScore):
        y = 100 - self.score
        if y < 25:
            compare = y
        else:
            compare = 25

        if turnScore > compare:
            return 'h'
        else:
            time.sleep(.5)
            return 'r'


# In[139]:


class Human(Player):

    def ask(self, turnScore):
        print ('---' + self.name + '---')
        choice = raw_input("Do you want to roll or hold? (r/h): ")
        while choice.lower()[0] != 'r' and choice.lower()[0] != 'h':
            print ('Sorry, I dont understand.')
            choice = raw_input("Do you want to roll or hold? (r/h): ")
        else:
            return choice


# In[140]:


class PlayerFactory(object):

    def getPlayer(self, kind):
        if kind[0].lower() == 'c':
            return Computer()
        if kind[0].lower() == 'h':
            return Human()


# In[141]:


class Game(object):
    def __init__(self, players=[]):
        self.turnScore = 0
        self.players = []
        self.dice = Dice()
        fac = PlayerFactory()

        for player in players:
            self.players.append(fac.getPlayer(player))

        self.playerIdx = random.randint(0, len(self.players) - 1)
        self.currentPlayer = self.players[self.playerIdx]


# In[142]:


def ask(self):
    return self.currentPlayer.ask(self.turnScore)


def maxScore(self):
    maxScore = 0
    for player in self.players:
        if (player.score > maxScore):
            maxScore = player.score
    return maxScore


def changePlayer(self):
    self.playerIdx = (self.playerIdx + 1) % len(self.players)
    self.turnScore = 0
    self.currentPlayer = self.players[self.playerIdx]


# In[143]:


def turn(self):
        
        rolled = self.dice.roll()
        print ('\n' + self.getCurrentPlayerName() + ', you rolled ' + str(rolled))
        if rolled == 1:
            print ('You rolled a 1 so your turn is over. You lost ' +                 str(self.turnScore) + ' possible points.')
            print ('Your current score is ' + str(self.getCurrentPlayerScore()) +             '\n')
            self.changePlayer()
            print ('Next up: ' + self.getCurrentPlayerName())
        else:
            self.turnScore += rolled
            print ('Your score this turn is ' + str(self.turnScore))
            print ('Your overall saved score is ' +             str(self.getCurrentPlayerScore()) + '\n')


# In[144]:


def addToScore(self):
        self.currentPlayer.addToScore(self.turnScore)

def getCurrentPlayerName(self):
        return self.currentPlayer.name
    

def getCurrentPlayerScore(self):
        return self.currentPlayer.score
    

def continueToPlay(self):
        if self.getCurrentPlayerScore() >= 100:
            return False
        else:
            return True


# In[145]:


def nextTurn(self):
        if self.ask()[0].lower() == 'r':
            self.turn()
        else:
            self.addToScore()
            print ('You decided to keep {0}\n'.format(self.getCurrentPlayerScore()))
            if self.continueToPlay():
                self.changePlayer()
                print ('Next up: ' + self.getCurrentPlayerName())
                print ('Your current score: ' + str(self.getCurrentPlayerScore()))


# In[146]:


class TimedGameProxy(Game):
    def __init__(self, players=[]):
        self.start = time.time()
        self.timed = 60
        self.game = Game(players)
        
        
    def nextTurn(self):
        return self.game.nextTurn()

    def continueToPlay(self):
        if self.game.currentPlayer.score > 100:
            return False
        timeLeft = time.time() - self.start
        if timeLeft > self.timed:
            if self.game.players[0].score > self.game.players[1].score:
                self.game.currentPlayer = self.game.players[0]
            else:
                self.game.currentPlayer = self.game.players[1]
            print ('\n Time is up! Game Over!')
            return False
        else:
            timeLeftNow = round((self.timed - timeLeft), 1)
            print ('There are {0} seconds left in the game'.format(timeLeftNow))
            return True


# In[147]:


def getCurrentPlayerName(self):
        return self.game.currentPlayer.name

def getCurrentPlayerScore(self):
        return self.game.currentPlayer.score


# In[148]:


def main():
    player1 = args.player1
    player2 = args.player2
    timed = args.timed
    
    try:
        if timed[0].lower() == 'y':
            game = TimedGameProxy([player1, player2])
        else:
            game = Game([player1, player2])
    except:
        game = Game([player1, player2])

    print ('Up first is ' + game.getCurrentPlayerName())

    while game.continueToPlay():
        game.nextTurn()

    print ('''\n*******************
        \n{0} wins with a score of {1}
        \n*******************'''.format(
        game.getCurrentPlayerName(), game.getCurrentPlayerScore()))
    sys.exit()
    
main()

