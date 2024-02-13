from ctypes.wintypes import tagRECT
import os
import pickle
from tabulate import tabulate
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
        self._discription=newDiscription

def checkDataExixtance():
    print("")
    print("********************")
    print("** checking data ***")
    if(os.path.exists('data.txt')):
      print("** data exists *****")

    else:
      print("data doesn't exists")
      print("please add data to the dirctory")
      print("bye")


def printCat():
    cat_art = """
********************
*    /\_/\\         *
*   ( o.o )        *
*    > ^ <         *
********************"""
    print(cat_art)

def clearData():
    with open('data.txt', 'w') as file:
        pass

#for obj in objs_loaded:
#    print(obj.name, obj.position,obj.discription)

def writeData():
    with open('data.txt', 'wb') as file:
        pickle.dump(objs_loaded, file)

def main():
    print("This is the main function.")

def printFunction():
    print("********************")
    print("*1.find an item ****")
    print("*2.change an item **")
    print("*3.delete an item **")
    print("*4.add an item *****")  
    print("*5.show all items **")
    print("*6.quit ************")
    print("********************")

def quit():
    clearData()
    writeData()
    
def findMyThing():
    itemName=input("the name of the item please : ")
    for target in objs_loaded:
        if(target.name == itemName):
            print("success")
            print(target.name+" located at "+ target.position)
            print("the discription: "+target.discription)
            break
        else:
            print("failed to find your item")

            print("please check your input and the data")

def changeMyThing():
    targetName=input("name of the item to be changed : ")
    for target in objs_loaded:
        if(target.name == targetName):
            print("successfully find the item")
            changeName=input("name to be changed to : ")
            changePosition=input("position to be changed to : ")
            changeDiscription=input("discription to be changed to : ")
            target.name=changeName
            target.position=changePosition
            target.discription=changeDiscription
            print("successful changed the item! ")
            break
        else:
            print("target to be changed not found")

    
def deleteItem():

    itemName=input("the name of the item please : ")
    now=0
    for target in objs_loaded:
        if(target.name == itemName):
            print("successfully find the item")
            print("deleting")
            objs_loaded.remove(objs_loaded[now])
            print("successfully delete the item "+ itemName)
            break
        else:
            print("failed to find your item")

            print("please check your input and the data")
        now+=1
def addItem():
    
    itemName=input("the name of the item to be added please : ")
    itemPosition=input("the position of the item to be added please : ")
    itemDiscription=input("the discription of the item to be added please : ")
    newItem= Cell(itemName,itemPosition,itemDiscription)
    objs_loaded.append(newItem)
    print("successfully add the item")

def showAllItem():
    #for target in objs_loaded:
        #print("name\t\tposition\t\tdiscription")
        #print(target.name+"\t\t"+ target.position+"\t\t"+target.discription)
    properties = [[obj.name, obj.position, obj.discription] for obj in objs_loaded]

# 输出表格
    print(tabulate(properties, headers=["Name", "Age", "Gender"], tablefmt="grid"))
    print("successfully show the lists of all items")


#cell_t=[Cell("1","0 1","null"),Cell("2","0 2","null")]

#with open('data.txt', 'wb') as file:
#    pickle.dump(cell_t, file)


with open('data.txt', 'rb') as file:
    objs_loaded = pickle.load(file)


if __name__ == "__main__":
    checkDataExixtance() 
    printCat()
    while(1):    
        printFunction()
        choice = int(input("input your choice: "))
        if choice ==1:
            findMyThing()
            print("choice_1 completed")
        elif choice ==2:
            changeMyThing()
            print("choice_2 completed")
            
        elif choice ==3:
            deleteItem()
            print("choice_3")

        elif choice ==4:
            addItem()
            print("choice_4")
        elif choice == 5:
            showAllItem()
            print("****list of all items****")
        elif choice ==6:
            print("quiting")
            quit()
            print("quit success")
            break
        else:
            print("please input correct number\n")

 
