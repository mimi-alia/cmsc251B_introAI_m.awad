# shopSmart.py
# ------------
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
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop
from functools import reduce

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    #take in list of fruit and weight, and a list of shops
    #return which shop  in which order costs least
    
    #list to stores total price for each order
    prices = []

    
    #for each shop, calculate the total price for each fruit in the order
    # add to prices list, where each inner list represents price for
    
    for shop in fruitShops:
        #list of total price for each fruit quanitity per order
        price = []
        for item in orderList:
            #get the cost of the fruit per unit
            cost = shop.getCostPerPound(item[0])
    ################################################################
                    ##debugging code##
    ################################################################
            #add the name of the fruit
            #price.append(item[0])
            #add the cost of the fruit
            #price.append(cost)
    ################################################################
            #add the price of the fruit per order
            price.append(item[1] * cost)
        #sum of the price for the entire order
        total = reduce(lambda x,y: x+y,price)
        prices.append((total))
    
    #select the cheapest price in the list of prices per order
    cheapest = min(prices)
    
    #use the index of the cheapest price to select the shop that has the
    #cheapest price
    return fruitShops[prices.index(cheapest)]      



if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops))#.getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops))#.getName())
