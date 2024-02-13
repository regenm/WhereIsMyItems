import os
import pickle
# check out if  data exists


class Cell:

    def __init__(self,name,position,discription):
        self._name = name 
        self._position = position
        self._discription =discription
    @property
    def name(self):
        return self._name
    
    @property
    def position(self):
        return self._position
    
    @property
    def discription(self):
        return self._discription
    


    @name.setter
    def name(self,newName):
        self._name=newName
    
    @position.setter
    def position(self,newPosition):
        self._position=newPosition
    
    @discription.setter
    def discription(self,newDiscription ):
        self._position=newDiscription


cell_t=[Cell("1","0 1","null"),Cell("2","0 2","null")]

with open('data.txt', 'wb') as file:
    pickle.dump(cell_t, file)