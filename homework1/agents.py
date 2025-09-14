from game import Agent
from game import Directions
from game import Actions
from random import random

class BasicAgent(Agent):
  """This agents just heads North until it cannot move"""
  def getAction(self, state):
    #return Directions.NORTH --Exception: Illegal action North
    #return state.NORTH --AttributeError: 'GameState' object has no attribute 'NORTH'
    #return state.getLegalPacmanActions() #--Exception: Illegal action ['South', 'West', 'Stop']
    random_num = int(len(state.getLegalPacmanActions()) * random())
    return state.getLegalPacmanActions()[random_num]
    
    