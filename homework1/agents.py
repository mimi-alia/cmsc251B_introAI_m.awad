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
    return state.getLegalPacmanActions()[0]

class RandomAgent(Agent):
    def getAction(self, state):
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
            print(state.getPacmanPosition())                
            return choice
        #if the length of options is only one, return that value
        else:
            choice = state.getLegalPacmanActions()[0]
            return choice
            print("length less than 2"+choice)
            
class ReflexAgent(Agent):
    def getAction(self, state):

        #examines possible one-step moves EXCEPT "Stop"
        #selects a random one of those moves that has a pellet 
        #if none, then a random move other than "Stop" should be returned
        
        ##access grid positions and push towards location
        positions = []
        if state.getPacmanPosition() not in positions:
            positions.append(state.getPacmanPosition())
            
        for i in range(len(state.getFood())):
            for j in range(len(state.getFood())[i]):
                if matrix[i][j] == element:
                    positions.append((i, j))
        
        currentFood = state.getFood()
        #if currentFood[x][y] == True:
            
        # get current location from state.getPacmanState() class
        
        # get current location from state.getPacmanPosition() tuple
        #current_position = [[*state.getPacmanPosition()]]
        
        #get location of the food pellet(s)
        #current_food = state.getFood()
        
        # if the current position does not contain a pellet, move
        for x,y in current_position:
            if current_food[x][y] == False:
                filtered = list(filter(lambda x: x != "Stop", state.getLegalPacmanActions()))
                random_num = int(len(filtered) * random())
                choice = filtered[random_num]
                print(choice)
                print(state.getPacmanPosition())
                return choice
            else:
                choice = "Stop"
        
        #asses coordinate location of current_food and put pacman there
        #how do you do that for a Grid object?
            
        
        
        #print(type(state.getPacmanState()))
        #print(state.getFood()[5][5] == True)
        #print(current_position)
        

            
        
