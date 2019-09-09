import re
import sys
import time
import os
import subprocess
from com.dtmilano.android.viewclient import ViewClient, View, ViewClientOptions
import copy

class stateNode:

    # Static variable keeping count of the number of states generated until now
    currentNumStates = 0

    def __init__(self, roadMap = [], attributesDictionary = {}, father = None):
        # Setting unique name
        self.name = 'state' + str(stateNode.currentNumStates)
        stateNode.incrementNumStates()
        # Setting the roadmap (list of UI elements) to get here
        self.roadMap = roadMap[:]
        # Setting the 'UI element -> attributes dictionary' dictionary (nested dictionary)
        self.attributesDictionary = copy.deepcopy(attributesDictionary)
        # Setting the 'UI element -> arriving state' dictionary
        self.outgoingStateDictionary = {}
        # Setting the father state
        self.father = father

        # Building the queue of UI elements to visit (key is UI element)
        self.visitQueue = []
        for key in self.attributesDictionary:
            self.visitQueue.append(key)


    # This method sets all over again the attributes dictionary and also their queue
    def updateAttributes(self, attributesDictionary = {}):
        # Setting the 'UI element -> attributes dictionary' dictionary (nested dictionary)
        self.attributesDictionary = copy.deepcopy(attributesDictionary)
        # Building the queue of UI elements to visit (key is UI element)
        del self.visitQueue[:]
        self.visitQueue = []
        for key in self.attributesDictionary:
            self.visitQueue.append(key)

    # This method returns and pops from the list the UI element that we have to analyze
    def popUIelementToAnalyze(self):
        if len(self.visitQueue) == 0:
            return None
        else:
            return self.visitQueue.pop(0)

    # This method adds a state that can be reached through a specific UI element (UiElement is actually an uniqueID)
    def addOutgoingState(self, UiElement, state):
        self.outgoingStateDictionary[UiElement] = state

    # This method increments the static num of states
    @classmethod
    def incrementNumStates(cls):
        cls.currentNumStates = cls.currentNumStates + 1

    def updateOutgoingStateDictionary(self, dictionary):
        self.outgoingStateDictionary = copy.deepcopy(dictionary)

    def getOutgoingStateDictionary(self):
        return self.outgoingStateDictionary

    def getStateName(self):
        return self.name

    def getCurrentQueueLength(self):
        return len(self.visitQueue)

    def getAttributesDictionary(self):
        return self.attributesDictionary

    def getRoadMap(self):
        return list(self.roadMap)

    def getFather(self):
        return self.father