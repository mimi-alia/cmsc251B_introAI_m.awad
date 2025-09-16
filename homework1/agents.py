#**************************************************************************
# Results:
# RandomAgent: 
# 	Mean: 238.0
# 	STDDev: N/A
# ReflexAgent:
# 	Mean: 
# 	STDDev: 
#**************************************************************************

from game import Agent
from game import Directions
from game import Actions
from random import random


class BasicAgent(Agent):
  """This agents just heads North until it cannot move"""
  def getAction(self, state):
    # a legal pacman action from the array is chosen, thus no error codes returned
    #however, it becomes an infinite action, so do not run
    #return state.getLegalPacmanActions()[0]
    
    #random agent
        #create a random number based on the length of state.getLegalPacmanActions()
        #arr to index the array with at the call
        
        #index the state.getLegalPacmanActions() arr with the random int
        
        #make it so it only chooses stop if others not available
        #get current positoin of pacman
        
        #If the length of the list of legal actions is more than a single option
        if len(state.getLegalPacmanActions()) > 1:
            #remove any option that equals stop if it exists
            filtered = list(filter(lambda x: x != "Stop", state.getLegalPacmanActions()))
            
            #get the length of that filtered list and pick a random number
            #from zero to the length to index with
            random_num = int(len(filtered) * random())
            
            #index the filtered list with the randomly selected index
            choice = filtered[random_num]
            print(choice)                
            return choice
        #if the length of options is only one, return that value
        else:
            choice = state.getLegalPacmanActions()[0]
            return choice
            print("length less than 2"+choice)
        
            
        
