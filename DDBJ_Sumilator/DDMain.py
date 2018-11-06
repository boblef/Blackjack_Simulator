#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:35:51 2018

@author: Bob
"""

import numpy as np
import csv
import xlrd
import math

class Player():
    
    #Constructor
    def __init__(self):
        #################################################################
        self.playerDeck = np.array([2,3,4,5,6,7,8,9,10,10,10,10,111])
        #################################################################
        #For making dataframe of specific true count
        #self.playerDeck = np.array([[2,3,4,10,6,7,8,9,10,10,10,10,111],
        #                            [2,3,4,5,10,7,8,9,10,10,10,10,111],
        #                            [2,10,4,5,6,7,8,9,10,10,10,10,111],
        #                            [10,3,10,5,6,7,8,9,10,10,10,10,111],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0]])
        #################################################################
        self.playerHand = []
        self.xl_bk = xlrd.open_workbook("DDStrategy.xlsx") #Open an xl file
        self.xl_sh = self.xl_bk.sheet_by_index(0) #Open first sheet of the xl file when player has just 2 cards
        self.xl_sh2 = self.xl_bk.sheet_by_index(1) #Open second sheet of the xl file when player has greater than equal to 3 cards
        
        self.playerHas = [0,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,120,119,118,117,116,115,114,113] #This is for index of xl
        self.playerHasSame = {"26":222, "27":20, "28":18, "29":16, "30":14, "31":12, "32":10, "33":8, "34":6, "35":4} #This is also index of xl file but just for a pairs
        self.xl_dealerHas = {"1":2, "2":3, "3":4, "4":5, "5":6, "6":7, "7":8, "8":9, "9":10, "10":111} #This is column index
        
        self.playerSum = 0 #The sum of player hand
        self.xl_col_index = 0 #col index of the xl file
        self.xl_row_index = 0 #row index of the xl file
    #End constructor
    
    def getPlayerHand(self):
        return self.playerHand
    #End getPlayerHand
    
    #################################################################################
    #################################################################################
    #giveCardToPlayer does that get an index from driver and pass it to the deck and build player hand.Then return it
    def giveCardToPlayer(self, index):
        self.playerHand.append(self.playerDeck[index])
        return self.playerHand
    #End giveCardtoPlayer
    
    #################################################################################
    #For making dataframe of specific true count
    #def giveCardToPlayer(self,row,col):
    #    self.playerHand.append(self.playerDeck[row][col])
    #    return self.playerHand
    #################################################################################
    #################################################################################
    
    
    
    
    
    #################################################################################
    #################################################################################
    def cardOfDeck(self,index):
        return self.playerDeck[index]
    #End cardOfDeck
    
    #################################################################################
    #For making dataframe of specific true count
    #def cardOfDeck(self,row,col):
    #    return self.playerDeck[row][col]
    #################################################################################
    #################################################################################
    
    def playerDouble(self):
        print("Player double")
    #End playerDouble
        
    
    def playerSplit(self, dealerHas):
        firstNum = self.playerHand[0]
        length = len(self.playerHand)
        split = 0
        counter = 0
        self.playerHand = [[firstNum for x in range(1)] for y in range(split + 2)]
            
        while length + split  > counter:
            inph = self.playerHand[counter]
            row, col = main.pickUpLocations()
            inph = inph.append(self.playerDeck[col])
            if inph[0] == inph[1]:
                split += 1
                self.playerHand = self.playerHand.append([firstNum])
                inph.pop(-1)
                continue
            else:
                while player.checkPlayerHandSplit(dealerHas) != "PB" or player.checkPlayerHandSplit(dealerHas) != "S":
                    row, col = main.pickUpLocations()
                    inph = inph.append(self.playerDeck[col])
                counter += 1
    #End playerSplit
    
    def checkPlayerHandSplit(self, dealerHas, index):
        ph = self.playerHand[index]
        #Get the sum of player hand
        self.playerSum = int(sum(ph))
        #Get colmn index from "xl_dealerHas". Pass "dealerHas" to the Hash which return a key of the Value.
        self.xl_col_index = [key for key, value in self.xl_dealerHas.items() if value == dealerHas] 
        
        #Player can "PlayerHit", "PlayerStay", "PlayerDouble", "PlayerSplit" and "PlayerBurst", if the player has just 2 cards.
        if len(ph) == 2:
            if self.playerSum == 121:
                return "S"
        
            elif int(ph[0]) != int(ph[1]):
                self.xl_row_index = self.playerHas.index(self.playerSum)
                return self.xl_sh.cell_value(int(self.xl_row_index),int(self.xl_col_index[0]))
        
            else: #self.playerHand[0] == self.playerHand[1]:
                self.xl_row_index = [key for key, value in self.playerHasSame.items() if value == self.playerSum]
                #print("The best way is ", self.xl_sh.cell_value(int(self.xl_row_index[0]), int(self.xl_col_index[0])))
                return self.xl_sh.cell_value(int(self.xl_row_index[0]), int(self.xl_col_index[0]))
        #End if condition for len(self.playerhand) == 2
        
        #Player can "PlayerHit", "PlayerStay" and "PlayerBurst" if player has greater than equal to 3
        if len(ph) >= 3:
            #Fix the sum of playerHand, when it                 
            if self.playerSum >= 111:
                while int(math.log10(self.playerSum) + 1) > 2:
                    self.playerSum -= 100
                    if self.playerSum > 21:
                        self.playerSum -= 10                   
                    
            if (self.playerSum > 131) or ((self.playerSum > 21) and (self.playerSum < 111)): #Player burst
                return "PB"
            
            else: #int(self.playerHand[0]) != int(self.playerHand[1]):
                self.xl_row_index = self.playerHas.index(self.playerSum)
                return self.xl_sh2.cell_value(int(self.xl_row_index),int(self.xl_col_index[0]))            
            
        #End if condition for len(self.playerHand) >= 3        
    #End checkPlayerHandSplit
    
    
    #checkPlayerHand does that check if player got a bj.if not pick up the best way from excel file and return it.
    def checkPlayerHand(self, dealerHas):        
        #Get the sum of player hand
        self.playerSum = int(sum(self.playerHand)) 
        #Get colmn index from "xl_dealerHas". Pass "dealerHas" to the Hash which return a key of the Value.
        self.xl_col_index = [key for key, value in self.xl_dealerHas.items() if value == dealerHas] 
        
        #Player can "PlayerHit", "PlayerStay", "PlayerDouble", "PlayerSplit" and "PlayerBurst", if the player has just 2 cards.
        if len(self.playerHand) == 2:
            if (len(self.playerHand) == 2) and (self.playerSum == 121):#Check if player got a black jack. EX A(111) and something 10. #Player got an black jack
                return "PBJ"
        
            elif int(self.playerHand[0]) != int(self.playerHand[1]):
                self.xl_row_index = self.playerHas.index(self.playerSum)
                return self.xl_sh.cell_value(int(self.xl_row_index),int(self.xl_col_index[0]))
        
            else: #self.playerHand[0] == self.playerHand[1]:
                self.xl_row_index = [key for key, value in self.playerHasSame.items() if value == self.playerSum]
                #print("The best way is ", self.xl_sh.cell_value(int(self.xl_row_index[0]), int(self.xl_col_index[0])))
                return self.xl_sh.cell_value(int(self.xl_row_index[0]), int(self.xl_col_index[0]))
        #End if condition for len(self.playerhand) == 2
        
        #Player can "PlayerHit", "PlayerStay" and "PlayerBurst" if player has greater than equal to 3
        if len(self.playerHand) >= 3:
            #Fix the sum of playerHand, when it                 
            if self.playerSum >= 111:
                while int(math.log10(self.playerSum) + 1) > 2:
                    self.playerSum -= 100
                    if self.playerSum > 21:
                        self.playerSum -= 10
                                        
            if (self.playerSum > 131) or ((self.playerSum > 21) and (self.playerSum < 111)): #Player burst
                return "PB"
            
            else: #int(self.playerHand[0]) != int(self.playerHand[1]):
                self.xl_row_index = self.playerHas.index(self.playerSum)
                return self.xl_sh2.cell_value(int(self.xl_row_index),int(self.xl_col_index[0]))            
            
        #End if condition for len(self.playerHand) >= 3

    #End playerCheckHand
    
    def resetPlayerHand(self):
        self.playerHand = []
        self.playerSum = 0
        self.xl_col_index = 0
        self.xl_row_index = 0
    #End resetPlayerHand
#End Player class






class Dealer():
    #Constructor
    def __init__(self):
        #################################################################
        self.dealerDeck = np.array([2,3,4,5,6,7,8,9,10,10,10,10,111])
        
        #################################################################################
        #For making dataframe of specific true count
        #self.dealerDeck = np.array([[2,3,4,10,6,7,8,9,10,10,10,10,111],
        #                            [2,3,4,5,10,7,8,9,10,10,10,10,111],
        #                            [2,10,4,5,6,7,8,9,10,10,10,10,111],
        #                            [10,3,10,5,6,7,8,9,10,10,10,10,111],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0]])
        #################################################################
        self.dealerHand = np.array([])
        
        self.dealerSum = 0
    #End constructor
    
    #getDealerHand return dealerHand
    def getDealerHand(self):
        return self.dealerHand
    #End getDealerHand
    
    
    #################################################################################
    #################################################################################
    #giveCardToDealer does that get an index from driver and pass it to the deck and build dealer hand.Then return it
    def giveCardToDealer(self, index):
        self.dealerHand = np.append(self.dealerHand,self.dealerDeck[index])
        return self.dealerHand
    #End giveCardtoPlayer
    
    
    #################################################################################
    #For making dataframe of specific true count
    #def giveCardToDealer(self, row, col):
    #    self.dealerHand = np.append(self.dealerHand,self.dealerDeck[row][col])
    #    return self.dealerHand
    #################################################################################
    #################################################################################
    #checkDealerHand does that check if the sum of dealer hand is bigger than equal to 17.if yes, dealer stop to pick a cord.
    #If it's bigger than 21, dealer lose. If the sum is 117,it means soft seven teen so dealer has to hit.
    def checkDealerHand(self):
        self.dealerSum = int(sum(self.dealerHand))

        if self.dealerSum >= 111:
            while int(math.log10(self.dealerSum) + 1) > 2:
                self.dealerSum -= 100
                if self.dealerSum > 21:
                    self.dealerSum -= 10
                
        if (self.dealerSum == 21) and (len(self.dealerHand) == 2):
            return "BJ"
        elif (self.dealerSum > 131) or ((self.dealerSum > 21) and (self.dealerSum < 111) ):#Check if the sum of dealer hand is bursted or not.
            return "DB"
        
        elif self.dealerSum == 117:
            return "MORE"
        
        elif self.dealerSum >= 118 or (self.dealerSum >= 17 and self.dealerSum <= 21):
            return "DS"
        else:
            return "MORE"
    #End playerCheckHand
    
    def resetDealerHand(self):
        self.dealerHand = np.array([])
        self.dealerSum = 0
    #End resetDealerHand
#End Dealer class
    
class Main():
    
    def __init__(self,buyin,firstBet,goalAmount):
        #####################################################################
        ####################################################################
        self.shareDecks = np.array([[2,3,4,5,6,7,8,9,10,10,10,10,111]] * 8)
        #################################################################################
        #For making dataframe of specific true count
        #self.shareDecks = np.array([[2,3,4,10,6,7,8,9,10,10,10,10,111],
        #                            [2,3,4,5,10,7,8,9,10,10,10,10,111],
        #                            [2,10,4,5,6,7,8,9,10,10,10,10,111],
        #                            [10,3,10,5,6,7,8,9,10,10,10,10,111],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0]])
        ###################################################################
        
        
        ###################################################################
        self.playerResult = [] # W(win), L(lose), P(push), SL(split lose), SW(split win), SP(split push)
        self.checkDoubleInSplit = [1,1,1,1,1,1] #Store 1 or 2. If there is double in a split hand,2 will be stored.
        self.buyin = buyin
        self.originalUnit = firstBet
        self.betMoney = firstBet
        self.totalBet = 0
        self.totalWinning = 0
        self.splitTimes = 1 #How many times player split
        self.playerDouble = False #player double or not
        self.todaysResult = 0 #if player won or lose in a day
        self.goalAmount = goalAmount
        ###########################################################
        
        
        ###########################################################
        #Need to coment out, when you make a dataframe of specific true count
        self.cards = 0 #Number of how many cards already used
        self.cardCounting = 0 #Running count
        self.trueCount = 0 #true count
        #################################################################################
        #For making dataframe of specific true count
        #self.cards = 52 #Number of how many cards already used
        #self.cardCounting = 5 #Running count
        #self.trueCount = 5 #true count
        ###########################################################
        ###########################################################
    #End constructor
    
    def pickUpLocations(self):
        i = 1
        while True:
            row = np.random.randint(0,8)
            col = np.random.randint(0,13)
            i += 1
            if self.shareDecks[row,col] != 0:
                if self.shareDecks[row,col] <= 6:#This is about card counting
                    self.cardCounting += 1
                elif self.shareDecks[row,col] >= 10:
                    self.cardCounting -= 1
                    
                self.shareDecks[row,col] = 0
                self.cards += 1
                return row,col
            else:
                continue
    #End pickUpLocation
    
    def getShareDecks(self):
        return self.shareDecks
    #End getShareDecks
    
    def resultSplit(self, playerHand, dealerHand, counter):
        dealerSum = int(sum(dealerHand))
        playerSum = int(sum(playerHand[counter]))
        
        dealerSum = int(sum(dealerHand))
        playerSum = int(sum(playerHand[counter]))
        
        if playerSum >= 111:
            while int(math.log10(playerSum) + 1) > 2:
                playerSum -= 100
                if playerSum > 21:
                    playerSum -= 10

        if dealerSum >= 111:
            while int(math.log10(dealerSum) + 1) > 2:
                dealerSum -= 100
                if dealerSum > 21:
                    dealerSum -= 10
        
        if ((len(dealerHand) == 2) and (dealerSum == 21)) and ~((len(playerHand) == 2) and (playerSum == 21)):
            self.playerResult.append("SL")
            return "DBJPL"
        elif ((playerSum > dealerSum) and (playerSum <= 21)) or ((dealerSum > 21) and (playerSum <= 21)):
            self.playerResult.append("SW")
            return "Win"
        elif (playerSum > 21) or (playerSum < dealerSum <= 21):
            self.playerResult.append("SL")
            return "Lose"
        else:
            self.playerResult.append("SP")
            return "Push"
    #End resultSplit

    def playerResultFun(self, playerHand, dealerHand):                        
        playerSum = int(sum(playerHand))
        dealerSum = int(sum(dealerHand))

        if playerSum >= 111:
            while int(math.log10(playerSum) + 1) > 2:
                playerSum -= 100
                if playerSum > 21:
                    playerSum -= 10

        if dealerSum >= 111:
            while int(math.log10(dealerSum) + 1) > 2:
                dealerSum -= 100
                if dealerSum > 21:
                    dealerSum -= 10       
        
        if ((len(playerHand) == 2) and (playerSum == 21)) and ~((len(dealerHand) == 2) and (dealerSum == 21)):
            self.playerResult.append("W")
            return "PBJ"
        elif ((len(dealerHand) == 2) and (dealerSum == 21)) and ~((len(playerHand) == 2) and (playerSum == 21)):
            self.playerResult.append("L")
            return "DBJPL"
        elif ((playerSum > dealerSum) and (playerSum <= 21)) or ((dealerSum > 21) and (playerSum <= 21)):
            self.playerResult.append("W")
            return "Win"
        elif (playerSum > 21) or (playerSum < dealerSum <= 21):
            self.playerResult.append("L")
            return "Lose"
        else:
            self.playerResult.append("P")
            return "Push"
    #End result
    
    def bettingSystem(self):
        """
        i = 1
        winCount = 0
        #This is betting system of 1-3-2-5
        if (self.cardCounting >= 5):
            while len(self.playerResult) >= i:
                if self.playerResult[-i] == "W":
                    winCount += 1
                    i += 1
                else:
                    break
            winCount %= 4
            if winCount == 0:
                return 1
            elif winCount == 1:
                return 3
            elif winCount == 2:
                return 2
            elif winCount == 3:
                return 5
        else:
            return 1
        """
        
        """
        True count betting system 1
        self.trueCount = round(self.cardCounting*52/(104-self.cards),1)
        if self.trueCount >= 1.5:
            if self.trueCount >= 5.5:
                return 10
            else:
                return math.floor(2*self.trueCount - 1)
        else:
            return 1
        """
        i = 1
        winCount = 0
        while len(self.playerResult) >= i:
            if self.playerResult[-i] == "W":
                winCount += 1
                i += 1
            else:
                break
        winCount %= 2
        if (self.trueCount > 1.5) and (winCount == 1):
            return 2
        else:
            return 1
    #End bettingSystem

    def betSplit(self,pr,double=1):#This is for a hand after split
        self.totalBet = self.betMoney * self.checkDoubleInSplit[double]
        
        if pr == "PBJ":
            print("Player won")
            #self.buyin += self.betMoney * 2
            self.totalWinning += self.betMoney
            self.betMoney = self.originalUnit
        elif pr == "DBJPL":
            print("Player lose")
            #self.buyin -= self.betMoney
            self.totalWinning -= self.betMoney
            self.betMoney = self.originalUnit
        elif pr == "Win":
            print("Player won")
            #self.buyin += self.betMoney * 2 * self.checkDoubleInSplit[double]
            self.totalWinning += self.betMoney * self.checkDoubleInSplit[double]
            self.betMoney = self.originalUnit
        elif pr == "Lose":
            print("Player lose")
            #self.buyin -= self.betMoney * self.checkDoubleInSplit[double]
            self.totalWinning -= self.betMoney * self.checkDoubleInSplit[double]
            self.betMoney = self.originalUnit
        elif pr == "Push":
            print("Player push")
    #End betSplit
    
    def bet(self,pr,units):
        if self.playerDouble:
            self.totalBet = self.betMoney * 2
            self.playerDouble = False
        else:
            self.totalBet = self.betMoney
        
        if pr == "PBJ":
            print("Player won")
            #self.buyin += self.betMoney * 2.5
            self.totalWinning += self.betMoney * 1.5
            self.betMoney = self.originalUnit * units
            #self.buyin -= self.betMoney
            print("Next bet is ",self.betMoney)
        elif pr == "DBJPL":
            print("Player lose")
            self.totalWinning -= self.betMoney
            self.betMoney = self.originalUnit
            #self.buyin -= self.betMoney
            print("Next bet is ",self.betMoney)
        elif pr == "Win":
            print("Player won")
            #self.buyin += self.totalBet * 2
            self.totalWinning += self.totalBet
            self.betMoney = self.originalUnit * units
            #self.buyin -= self.betMoney
            print("Next bet is ",self.betMoney)
        elif pr == "Lose":
            print("Player lose")
            #self.buyin -= self.totalBet
            self.totalWinning -= self.totalBet
            self.betMoney = self.originalUnit
            #self.buyin -= self.betMoney
            print("Next bet is ",self.betMoney)
        elif pr == "Push":
            print("Player push")
            #self.buyin += self.totalBet
            
            
    #End bet
    
    def splitAction(self):#When player do split,this function will be called
        self.splitTimes += 1
    #End splitAction
    
    def doubleAction(self):
        #self.betMoney += self.originalUnit
        self.playerDouble = True
    #End doubleAction
    
    def getResult(self,playerHand):
        result = []
        i = 1
        if (self.playerResult[-1] == "SW") or (self.playerResult[-1] == "SL") or (self.playerResult[-1] == "SP"):
            while len(playerHand) >= i:
                if (self.playerResult[-i] != "W") or (self.playerResult[-i] != "L") or (self.playerResult[-i] != "P"):
                    result.insert(0,self.playerResult[-i])
                    i += 1
                else:
                    break
            return result
        else:
            return self.playerResult[-1]
    
    def checkMoney(self):
        if (self.totalWinning <= -self.buyin):
            return 1
        elif self.totalWinning >= self.goalAmount:
            self.todaysResult = 1
            return 1
        else:
            return 0
    #End checkMoney
    
    def resetMain(self):
        ##################################################################
        #Need to coment out, when you make a dataframe of specific true count
        self.cards = 0
        self.cardCounting = 0
        self.trueCount = 0
        #################################################################################
        #For making dataframe of specific true count
        #self.cards = 52
        #self.cardCounting = 5
        #self.trueCount = 5
        ##################################################################
        
        
        ###################################################################
        self.shareDecks = np.array([[2,3,4,5,6,7,8,9,10,10,10,10,111]] * 8)
        #################################################################################
        #For making dataframe of specific true count
        #self.shareDecks = np.array([[2,3,4,10,6,7,8,9,10,10,10,10,111],
        #                            [2,3,4,5,10,7,8,9,10,10,10,10,111],
        #                            [2,10,4,5,6,7,8,9,10,10,10,10,111],
        #                            [10,3,10,5,6,7,8,9,10,10,10,10,111],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                            [0,0,0,0,0,0,0,0,0,0,0,0,0]])
        ###################################################################
    #End resetMain
    
    def resetMainValues(self):#Need to reset every hand
        self.checkDoubleInSplit = [1,1,1,1,1,1]
        self.doubleTimes = 1
    #End resetMainValues
    
#End Main

class CollectingData():
    def __init__(self):
        self.playerHand = []
        self.playerFirstHand = []
        self.playerSum = 0
        self.playerFirstAction = ""
        self.dealerHand = []
        self.dealerShowCard = []
        self.dealerSum = 0
        self.result = ""
        self.firstBet = 0
        self.totalBet = 0
        self.totalWinning = 0
        self.cardCounting = 0
        self.trueCount = 0
        self.todaysResult = 0
        self.todaysAmount = 0
    #End constractor of CollectingData class
    
    def setPlayerHand(self,playerHand):
        self.playerHand = playerHand
    #End setPlayerHand
    
    def setPlayerFirstHand(self,playerFirstHand):
        self.playerFirstHand = playerFirstHand
    #End setPlayerFirstHand
    
    def setPlayerSum(self,playerHand):
        i = 0
        try:
            playerSum = [int(sum(i)) for i in playerHand]
            if playerSum[i] >= 111:
                while int(math.log10(playerSum[i]) + 1) > 2:
                    playerSum[i] -= 100
                    if playerSum[i] > 21:
                        playerSum[i] -= 10
            self.playerSum = playerSum
        except:
            playerSum = int(sum(playerHand))
            if playerSum >= 111:
                while int(math.log10(playerSum) + 1) > 2:
                    playerSum -= 100
                    if playerSum > 21:
                        playerSum -= 10
            self.playerSum = playerSum
    #End setPlayerSum
    
    def setPlayerFirstAction(self, action):
        self.playerFirstAction = action
    #End setPlayerFirstAction
    
    def setDealerHand(self,dealerHand):
        self.dealerHand = dealerHand
    #End setDealerHand
    
    def setDealerShowCard(self,dealerHand):
        self.dealerShowCard = int(dealerHand[0])
    #End setDealerShoeCard
    
    def setDealerSum(self,dealerSum):
        if dealerSum >= 111:
            while int(math.log10(dealerSum) + 1) > 2:
                dealerSum -= 100
                if dealerSum > 21:
                    dealerSum -= 10
        self.dealerSum = int(dealerSum)
    #End setDealerSum
    
    def setResult(self,result):
        self.result = result
    #End setResult
    
    def setFirstBet(self,bet):
        self.firstBet = bet
    #End setBetMoney
    
    def setTotalBet(self,tBet):
        self.totalBet = tBet
    #End sewtTotalBetMoney
    
    def setTotalWinning(self,total):
        self.totalWinning = total
    #End setTotalWinning
    
    def setCardCounting(self,counting):
        self.cardCounting = counting
    #End setCardCounting
    
    def setTrueCount(self, trueCount):
        self.trueCount = trueCount
    #End setTrueCount
    
    def setTodaysResult(self,todaysResult):
        self.todaysResult = todaysResult
    #End setTodaysResult
    
    def setTodaysAmount(self,amount):
        self.todaysAmount = amount
    #End setTodaysAmount
    
    def writeEachGameResultToCSV(self):
        playData = [self.playerFirstHand,self.playerFirstAction,self.playerHand,self.playerSum,self.dealerShowCard,self.dealerHand,\
                    self.dealerSum,self.result,self.totalWinning,self.cardCounting,self.trueCount]
        with open('DDBJpractice4.csv','a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(playData)
    #End writeEachGameResultToCSV
    
    def writeTodaysResultToCSV(self):
        todaysR = [self.todaysAmount,self.todaysResult]
        with open('B200_G100_10years_1/DDBJ10_b200_g100.csv','a') as f2:
            writer = csv.writer(f2, lineterminator='\n')
            writer.writerow(todaysR)
#End Collectingdata
    
#Make instances of each classes
player = Player()
dealer = Dealer()
main = Main(200,25,100)
collect = CollectingData()
#End instance

#Define variables
cards = 0
#playTimes = 50 #How many games player play
#while 1 <= playTimes:#This is first while roop
#print(playTimes,"times")
for i in np.arange(1,361,1):
    shota = True
    print(shota)
    while shota:
        ############################################
        ############################################
        #Need this block, when you make a data frame of specific true count
        #このブロックただ消すだけでいい
        #main.resetMain()
        ############################################
        ############################################
        if main.checkMoney():#Check if player burst or got the amount that player expected
            break
        #End if
        collect.setFirstBet(main.betMoney)
        collect.setCardCounting(main.cardCounting)
        collect.setTrueCount(main.trueCount)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Card counting :",main.cardCounting)
        print("True count :",main.trueCount)
        if 52 < main.cards:
            main.resetMain()
            continue
        
    
        counter2 = 0 #counter for inside split
        #################################################################################
        #################################################################################
        #Need to coment out, when you make a data frame of specific true count
        row, col = main.pickUpLocations()
        player.giveCardToPlayer(col)
        row1, col1 = main.pickUpLocations()
        playerHand = player.giveCardToPlayer(col1)
        
        row2, col2 = main.pickUpLocations()
        dealerHand = dealer.giveCardToDealer(col2)
        
        #################################################################################
        #For making dataframe of specific true count
        #row, col = main.pickUpLocations()
        #player.giveCardToPlayer(row,col)
        #row1, col1 = main.pickUpLocations()
        #playerHand = player.giveCardToPlayer(row1,col1)
        
        #row2, col2 = main.pickUpLocations()
        #dealerHand = dealer.giveCardToDealer(row2,col2)
        #################################################################################
        #################################################################################
        
        print("Player's first hand : ", playerHand)
        print("Dealer show card : ", dealerHand)
        
        collect.setPlayerFirstHand([player.playerHand[0],player.playerHand[1]])
        collect.setDealerShowCard(dealer.dealerHand)
        bestWay = player.checkPlayerHand(int(dealerHand[0]))
        collect.setPlayerFirstAction(bestWay)
        while True: #This is second(inner) while roop
            bestWay = player.checkPlayerHand(int(dealerHand[0]))
            print("The best way is ",bestWay)
            
        
            if bestWay == "H":
                #########################################################################
                #########################################################################
                #Need to coment out, when you make a dataframe of specific true count
                row, col = main.pickUpLocations()
                player.giveCardToPlayer(col)
                
                #################################################################################
                #For making dataframe of specific true count
                #row, col = main.pickUpLocations()
                #player.giveCardToPlayer(row,col)
                #########################################################################
                #########################################################################
            elif bestWay == "S":
                print("Player' hand : ",player.playerHand)
                while True:#This is third(inner of inner) while roop
                    #####################################################################
                    #####################################################################
                    #Need to coment out.when you make a dataframe of specific true count
                    row, col = main.pickUpLocations()
                    dealer.giveCardToDealer(col)
                    
                    #################################################################################
                    #For making dataframe of specific true count
                    #row, col = main.pickUpLocations()
                    #dealer.giveCardToDealer(row,col)
                    #####################################################################
                    #####################################################################
                    cdh = dealer.checkDealerHand()
                    if cdh == "BJ":
                        print("Dealer's hand : ",dealer.dealerHand)
                        pr = main.playerResultFun(player.playerHand, dealer.dealerHand)
                        if pr == "DBJPL":
                            bs = main.bettingSystem()
                            main.bet(pr, bs)
                        elif pr == "Push":
                            bs = main.bettingSystem()
                            main.bet(pr, bs)
                        break #Third while roop break and go back to second roop
                    
                    elif cdh == "DB":
                        print("Dealer7s hand : ",dealer.dealerHand)
                        pr = main.playerResultFun(player.playerHand, dealer.dealerHand)
                        bs = main.bettingSystem()
                        main.bet(pr, bs)
                        break#Third while roop break and go back to second roop
                    
                    elif cdh == "DS":
                        print("Dealer's hand : ",dealer.dealerHand)
                        pr = main.playerResultFun(player.playerHand, dealer.dealerHand)
                        bs = main.bettingSystem()
                        main.bet(pr, bs)
                        break#Third while roop break and go back to second roop
                    else:
                        continue
                break#Second while roop break and go back to first while roop
        
            elif bestWay == "D":
                main.doubleAction()
                ##############################################################
                ##############################################################
                #Need to coment out,when you make a dataframe of specific true count
                row, col = main.pickUpLocations()
                player.giveCardToPlayer(col)
                
                #################################################################################
                #For making dataframe of specific true count
                #row, col = main.pickUpLocations()
                #player.giveCardToPlayer(row,col)
                ##############################################################
                ##############################################################
                print("Player's hand : ", player.getPlayerHand())
    
                while True:#This is third(inner of inner) while roop
                    ##########################################################
                    ##########################################################
                    #Need to coment out, when you make a dataframe of specic true count
                    row, col = main.pickUpLocations()
                    dealer.giveCardToDealer(col)
                    
                    #################################################################################
                    #For making dataframe of specific true count
                    #row, col = main.pickUpLocations()
                    #dealer.giveCardToDealer(row,col)
                    ##########################################################
                    ##########################################################
                    cdh = dealer.checkDealerHand()
                    if cdh == "BJ":
                        pr = main.playerResultFun(player.playerHand, dealer.dealerHand)
                        bs = main.bettingSystem()
                        main.bet(pr, bs)
                        print("Dealer's hand : ",dealer.dealerHand)
                        break#Third while roop break and go back to second while roop
                    
                    elif cdh == "DB":
                        print("Dealer's hand : ",dealer.dealerHand)
                        pr = main.playerResultFun(player.playerHand, dealer.dealerHand)
                        bs = main.bettingSystem()
                        main.bet(pr, bs)
                        break#Third while roop break and go back to second while roop
                    
                    elif cdh == "DS":
                        print("Dealer's hand : ",dealer.dealerHand)
                        pr = main.playerResultFun(player.playerHand, dealer.dealerHand)
                        if pr == "Win":
                            bs = main.bettingSystem()
                            main.bet(pr, bs)
                            break#Third while roop break and go back to second while roop
                        elif pr == "Lose":
                            bs = main.bettingSystem()
                            main.bet(pr, bs)
                            break#Third while roop break and go back to second while roop
                        elif pr == "Push":
                            bs = main.bettingSystem()
                            main.bet(pr, bs)
                            break#Third while roop break and go back to second while roop
                    else:
                        continue
                break#Second while roop break and go back to first while roop
            
            elif bestWay == "SP":
                main.splitAction()
                firstNum = player.playerHand[0]
                length = len(player.playerHand)
                split = 0
                counter = 0
                player.playerHand = [[firstNum for x in range(1)] for y in range(split + 2)]
                print("After first split : ",player.playerHand)
                    
                while length + split  > counter:#This is third(inner of inner) while roop
                    #inph = player.playerHand[counter]
                    #####################################################################
                    #####################################################################
                    #Need to coment out, when you make a dataframe of specific true count
                    row, col = main.pickUpLocations()
                    player.playerHand[counter] = np.append(player.playerHand[counter],player.cardOfDeck(col))
                    
                    
                    #################################################################################
                    #For making dataframe of specific true count
                    #row, col = main.pickUpLocations()
                    #player.playerHand[counter] = np.append(player.playerHand[counter],player.cardOfDeck(row,col))
                    #####################################################################
                    #####################################################################
                    print("This is player hand :",player.playerHand)
                    print("This is element of counter :",player.playerHand[counter])
                    
                    if firstNum == 111:
                        counter += 1
                        #####################################################################
                        #####################################################################
                        #Need to coment out, when youmake a dataframe of specific true count
                        row, col = main.pickUpLocations()
                        player.playerHand[counter] = np.append(player.playerHand[counter],player.cardOfDeck(col))
                        
                        
                        #################################################################################
                        #For making dataframe of specific true count
                        #row, col = main.pickUpLocations()
                        #player.playerHand[counter] = np.append(player.playerHand[counter],player.cardOfDeck(row,col))
                        #####################################################################
                        #####################################################################
                        #counter += 1
                        break
                        
                    if player.playerHand[counter][0] == player.playerHand[counter][1]:
                        print("An error is coming")
                        split += 1
                        main.splitAction()
                        player.playerHand[counter] = np.delete(player.playerHand[counter],[1])
                        #player.playerHand = np.append(player.playerHand,[[firstNum]])
                        player.playerHand.append([[firstNum]])
                        continue
                    else:
                        while True:#This is fourth(inner of inner of inner) while roop 
                            bestWay = player.checkPlayerHandSplit(int(dealerHand[0]), counter)
                            if bestWay == "PB":
                                break#Fourth while roop break and go back to third while roop
                            
                            elif bestWay == "S":
                                break#Fourth while roop break and go back to third while roop
                            
                            elif bestWay == "H":
                                #########################################################
                                #########################################################
                                #Need to coment out,when you make a dataframe of specific true count
                                row, col = main.pickUpLocations()
                                player.playerHand[counter] = np.append(player.playerHand[counter],player.cardOfDeck(col))
                                
                                #################################################################################
                                #For making dataframe of specific true count
                                #row, col = main.pickUpLocations()
                                #player.playerHand[counter] = np.append(player.playerHand[counter],player.cardOfDeck(row,col))
                                #########################################################
                                #########################################################
                            elif bestWay == "D":
                                main.checkDoubleInSplit[counter] = 2
                                #########################################################
                                #########################################################
                                #Need to coment out, when you make a dataframe of specific true count
                                row, col = main.pickUpLocations()
                                player.playerDouble()
                                player.playerHand[counter] = np.append(player.playerHand[counter],player.cardOfDeck(col))
                                
                                
                                #################################################################################
                                #For making dataframe of specific true count
                                #row, col = main.pickUpLocations()
                                #player.playerDouble()
                                #player.playerHand[counter] = np.append(player.playerHand[counter],player.cardOfDeck(row,col))
                                #########################################################
                                #########################################################
                                break#Fourth while roop break and go back to third while roop
                            
                            elif bestWay == "SP":
                                break#Fourth while roop break and go back to third while roop
                        counter += 1
                
                print("Player's hand : ",player.playerHand)
                while True:#This is third(inner of inner) while roop
                    #####################################################################
                    #####################################################################
                    #Need to coment out, when you make a dataframe of specific true count
                    row, col = main.pickUpLocations()
                    dealer.giveCardToDealer(col)
                    
                    
                    #################################################################################
                    #For making dataframe of specific true count
                    #row, col = main.pickUpLocations()
                    #dealer.giveCardToDealer(row,col)
                    #####################################################################
                    #####################################################################
                    cdh = dealer.checkDealerHand()
                                    
                    if cdh == "BJ":
                        print("Dealer's hand : ",dealer.dealerHand)
                        pushCounter = 0
                        if firstNum == 111:
                            while counter >= 0:
                                pr = main.resultSplit(player.playerHand, dealer.dealerHand, counter2)
                                counter2 += 1
                                counter -= 1
                                if pr == "Push":
                                    pushCounter += 1
                            if pushCounter < 2:
                                main.betSplit("DBJPL")
                            else:
                                main.betSplit("Push")
                            break#Third while roop break and go back to second while roop
                        else:
                            while counter > 0:
                                pr = main.resultSplit(player.playerHand, dealer.dealerHand, counter2)
                                counter2 += 1
                                counter -= 1
                                if pr == "Push":
                                    pushCounter += 1
                            if pushCounter < 2:
                                main.betSplit("DBJPL")
                            else:
                                main.betSplit("Push")
                            break#Third while roop break and go back to second while roop
                    
                    elif cdh == "DB":
                        print("Dealer's hand : ",dealer.dealerHand)
                        if firstNum == 111:
                            while counter >= 0:#This is fourth(inner og inner of inner) while roop
                                pr = main.resultSplit(player.playerHand, dealer.dealerHand, counter2)
                                main.betSplit(pr,counter2)
                                counter2 += 1
                                counter -= 1
                            break#Fourth while roop break and go back to third while roop
                        else:
                            while counter > 0:#This is fourth(inner og inner of inner) while roop
                                pr = main.resultSplit(player.playerHand, dealer.dealerHand, counter2)
                                main.betSplit(pr,counter2)
                                counter2 += 1
                                counter -= 1
                            break#Fourth while roop break and go back to third while roop
                    
                    elif cdh == "DS":
                        if firstNum == 111:
                            while counter >= 0:#This is fourth(inner of inner of inner) while roop
                                print("Dealer's hand : ",dealer.dealerHand)
                                pr = main.resultSplit(player.playerHand, dealer.dealerHand, counter2)
                                if pr == "Win":
                                    main.betSplit(pr,counter2)
                                    counter2 += 1
                                    counter -= 1
                                elif pr == "Lose":
                                    main.betSplit(pr,counter2)
                                    counter2 += 1
                                    counter -= 1
                                elif pr == "Push":
                                    counter2 += 1
                                    counter -= 1
                                else:
                                    continue
                                #End fourth while
                            break#Fourth while roop break and go back to third while roop
                        else:
                            while counter > 0:#This is fourth(inner of inner of inner) while roop
                                print("Dealer's hand : ",dealer.dealerHand)
                                pr = main.resultSplit(player.playerHand, dealer.dealerHand, counter2)
                                if pr == "Win":
                                    main.betSplit(pr,counter2)
                                    counter2 += 1
                                    counter -= 1
                                elif pr == "Lose":
                                    main.betSplit(pr,counter2)
                                    counter2 += 1
                                    counter -= 1
                                elif pr == "Push":
                                    counter2 += 1
                                    counter -= 1
                                else:
                                    continue
                                #End fourth while
                            break#Fourth while roop break and go back to third while roop
                    else:
                        continue
                    break#Third while roop break and go back to second while roop
                break#Second while roop break and go back to first while roop
                
                        
            elif bestWay == "PB":
                print("Player's hand : ",player.playerHand)
                pr = main.playerResultFun(player.playerHand, dealer.dealerHand)
                bs = main.bettingSystem()
                main.bet(pr, bs)
                break#Second while roop break and go back to first while roop
            
            else: #player got a bj
                #########################################################################
                #########################################################################
                #Need to coment out, when you make a dataframe of specific true count
                row, col = main.pickUpLocations()
                dealer.giveCardToDealer(col)
                
                
                #################################################################################
                #For making dataframe of specific true count
                #row, col = main.pickUpLocations()
                #dealer.giveCardToDealer(row,col)
                #########################################################################
                #########################################################################
                pr = main.playerResultFun(player.playerHand, dealer.dealerHand)
                print("Dealer's hand : ",dealer.dealerHand)
                if pr == "PBJ":
                    bs = main.bettingSystem()
                    main.bet(pr, bs)
                break#Second while roop break and go back to first while roop
    
        collect.setPlayerHand(player.playerHand)
        collect.setPlayerSum(player.playerHand)
        collect.setDealerHand(dealer.dealerHand)
        collect.setDealerSum(int(sum(dealer.dealerHand)))
        collect.setResult(main.getResult(player.playerHand))
        collect.setTotalWinning(main.totalWinning)
        collect.setTotalBet(main.totalBet)
        #collect.writeEachGameResultToCSV()
        player.resetPlayerHand()
        dealer.resetDealerHand()
        main.resetMainValues()
        #playTimes -= 1
        print("This is current winning money : ",int(main.totalWinning))
        
    print("Player made this much money : ",int(main.totalWinning))
    print("Todaysresult : ",main.todaysResult)
    collect.setTodaysResult(main.todaysResult)
    collect.setTodaysAmount(main.totalWinning)
    print("You made :",collect.todaysAmount)
    collect.writeTodaysResultToCSV()
    ############################################
    ###########################################
    ############################################
    #Delete below
    player.resetPlayerHand()
    dealer.resetDealerHand()
    main.resetMainValues()
    main.totalWinning = 0
    main.todaysResult = 0
            
    ##############################
    ############################
    ###########################