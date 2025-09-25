# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class Node():
    def __init__(self, state, action=None, parent=None, path_cost=0, step_cost=0):
        self.state = state
        self.action = action
        self.parent = parent
        self.path_cost = path_cost
        self.step_cost = step_cost

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    ##save start state to local var
    initial_state = problem.getStartState()
    
    ##save successors of initial state to var
    initial_state_frontier = problem.getSuccessors(initial_state)
    
    ##initiate a new instance of util.Stack class object
    stack = util.Stack() 
    
    ##add frontier to stack object's list attribute
    
    [stack.push(x) for x in initial_state_frontier]
    
    
    ##initial explored list is an empty list
    explored = set()
    
    
    ##while frontier is not empty
    while len(stack.list) > 0:
        ##remove last item from stack list, save to variable
        current_state = stack.pop()
        
        ##get successors of the current state
        cur_frontier = problem.getSuccessors(current_state[0])
        
        ##since the state has been expanded, add it to explored
        explored.add(current_state)
           
        ##if solution found
        if (problem.isGoalState(current_state[0])):
            ##list of actions from s to g
            actions = [x[1] for x in explored]
            print("solution actions: ", actions)
            return actions
        ##if solution not found, push states to stack
        else:
                ##add any unnexplored successor to the stack
               for suc in cur_frontier:
                    if suc not in explored:
                        stack.push(suc)
                    else:
                        print("loser: ", explored)
                        return []
       ##this doesn't run properly and i dont know why. I followed proper
       ##logic so...
        
    
    print(problem.isGoalState((3,5)))
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    ##save start state to local var
    initial_state = problem.getStartState()
    
    ##save successors of initial state to var
    initial_state_frontier = problem.getSuccessors(initial_state)
    
    ##initiate a new instance of util.Queue class object
    queue = util.Queue() 
    
    ##add frontier to queue object's list attribute
    
    [queue.push(x) for x in initial_state_frontier]
    
    
    ##initial explored list is an empty list
    explored = set()
    
    
    ##while frontier is not empty
    while len(queue.list) > 0:
        ##remove last item from stack list, save to variable
        current_state = queue.pop()
        
        ##get successors of the current state
        cur_frontier = problem.getSuccessors(current_state[0])
        
        ##since the state has been expanded, add it to explored
        explored.add(current_state)
           
        ##if solution found
        if (problem.isGoalState(current_state[0])):
            ##list of actions from s to g
            actions = [x[1] for x in explored]
            print("solution actions: ", actions)
            return actions
        ##if solution not found, push states to queue
        else:
                ##add any unnexplored successor to the queue
               for suc in cur_frontier:
                    if suc not in explored:
                        queue.push(suc)
                    else:
                        print("loser: ", explored)
                        return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    ### I would solve this by calling dfs then bfs over each layer expanded
    ###after initial dfs search was called. this would require embedding
    ##iterations so that a depth is reached first, then every node is expanded
    ##on that same level
    
    
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
