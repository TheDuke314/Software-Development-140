"""
Author: Luke Hodge
Date: 12/18/2022
Program name: Rock Paper Scissors
Class: Software Development
This program allows you to play Rock Paper Scissors with the computer. After choosing rock, paper, or scissors the program will tell you
what the computer chose, your total number of games, number of games won, number of games lost, and number of games drawn.
"""
from breezypythongui import EasyFrame
from breezypythongui import EasyDialog
from tkinter import PhotoImage

#The main function which contains buttons, images, and variable initializations
class Final (EasyFrame): #creates a breezypythongui window

    def __init__ (self):# This function initializes the program window.
        EasyFrame.__init__(self, title = "Rock Paper Scissors")
        self.setResizable(True);#This allows the program to be resizable

        
        self.Game_Number = 0 # This variable is the number of games played
        self.Games_Won = 0 # This variable is the number of games won
        self.Games_Lost = 0#This variable is the number of games lost
        self.Games_Draw = 0#This variable is the number of games drawn
    
        #retrieves and and places the photo of Rock
        imageLabel_1 = self.addLabel(text="",row=3,column=2,columnspan=1,sticky="NSEW")
        self.image_1 = PhotoImage(file = "Rock.png")
        imageLabel_1["image"] = self.image_1
        #retrieves and and places the photo of paper
        imageLabel_2 = self.addLabel(text="",row=3,column=3,columnspan=1, sticky="NSEW")
        self.image_2 = PhotoImage(file = "Paper.png")
        imageLabel_2["image"] = self.image_2
        #retrieves and places the photo of scissors
        imageLabel_3 = self.addLabel(text="",row=3,column=4,columnspan=1, sticky="NSEW")
        self.image_3 = PhotoImage(file = "Scissors.png")
        imageLabel_3["image"] = self.image_3

        self.Cbutton = self.addButton(text="Rock", row=4, column=2, command= self.Rock)#A button which calls the function for choosing rock
        self.Cbutton = self.addButton(text="Paper", row=4, column=3, command= self.Paper)#A button which calls the function for choosing paper
        self.Cbutton = self.addButton(text="Scissors", row=4, column=4, command= self.Scissors)#A button which calls the function for choosing scissors
        self.Cbutton = self.addButton(text="Exit", row=1, column=3, command= self.Quit)#A button which calls the function for exiting the app
        self.Cbutton = self.addButton(text="Reset", row=1, column=4, command= self.Reset)#A button which calls the reset function

    #Function which Resets the values of number of games, games won, games lost, and games drawn
    def Reset(self):
        self.Game_Number = 0
        self.Games_Won = 0
        self.Games_Lost = 0
        self.Games_Draw = 0
        

        
    #Function which plays rock paper scissors with user's pick being rock
    def Rock(self):
        UserChoice = 1#Users choice of rock
        import random
        random_number = random.randint(1,3)#random number generated to pick what choice the computer chooses
        if UserChoice == random_number:#if statement for if computer chose rock
            self.Game_Number = self.Game_Number+ 1#Increases variable value of number of games
            self.Games_Draw = self.Games_Draw+ 1#Increases variable value of games drawn
            #message box which gives info on whether you won,lost, or drew the game, number of games, games won, games lost, games drawn
            self.messageBox(title = "Draw", message = "The Computer picked Rock. You have played a total of "+str(self.Game_Number) +" games. You have won "
                            +str(self.Games_Won)+ " games. You have lost " +str(self.Games_Lost)+" games. You have drawn " +str(self.Games_Draw)+" games." , height = 8, width = 30)
        elif UserChoice == 1 and random_number== 3:#if statement for if computer chose scissors
            self.Game_Number = self.Game_Number+ 1
            self.Games_Won = self.Games_Won+ 1#Increases variable value of games won
            self.messageBox(title = "You Win", message = "The Computer picked Scissors. You have played a total of "+str(self.Game_Number) +" games. You have won "
                            +str(self.Games_Won)+ " games. You have lost " +str(self.Games_Lost)+" games. You have drawn " +str(self.Games_Draw)+" games.", height = 8, width = 30)
        elif UserChoice == 1 and random_number== 2:
            self.Game_Number = self.Game_Number+ 1
            self.Games_Lost =self.Games_Lost+ 1#Increases variable value of games lost
            self.messageBox(title = "You Lose", message = "The Computer picked Paper. You have played a total of "+str(self.Game_Number) +" games. You have won "
                            +str(self.Games_Won)+ " games. You have lost " +str(self.Games_Lost)+" games. You have drawn " +str(self.Games_Draw)+" games." ,height = 8, width = 30)

    #Function which plays rock paper scissors with user's pick being Paper   
    def Paper(self):
        UserChoice = 2#Users choice of paper
        import random
        random_number = random.randint(1,3)#random number generated to pick what choice the computer chooses
        if UserChoice == random_number:
            self.Game_Number = self.Game_Number+ 1#Increases variable value of number of games
            self.Games_Draw = self.Games_Draw+ 1#Increases variable value of games drawn
            #message box which gives info on whether you won,lost, or drew the game, number of games, games won, games lost, games drawn
            self.messageBox(title = "Draw", message = "The Computer picked Paper. You have played a total of "+str(self.Game_Number) +" games. You have won "
                            +str(self.Games_Won)+ " games. You have lost " +str(self.Games_Lost)+" games. You have drawn " +str(self.Games_Draw)+" games." , height = 8, width = 30)
        elif UserChoice == 2 and random_number== 1:#if statement for if computer chose rock
            self.Game_Number = self.Game_Number+ 1
            self.Games_Won = self.Games_Won+ 1#Increases variable value of games won
            self.messageBox(title = "You Win", message = "The Computer picked Rock. You have played a total of "+str(self.Game_Number) +" games. You have won "
                            +str(self.Games_Won)+ " games. You have lost " +str(self.Games_Lost)+" games. You have drawn " +str(self.Games_Draw)+" games.", height = 8, width = 30)
        elif UserChoice == 2 and random_number== 3:#if statement for if computer chose scissors
            self.Game_Number = self.Game_Number+ 1
            self.Games_Lost =self.Games_Lost+ 1#Increases variable value of games lost
            self.messageBox(title = "You Lose", message = "The Computer picked Scissors. You have played a total of "+str(self.Game_Number) +" games. You have won "
                            +str(self.Games_Won)+ " games. You have lost " +str(self.Games_Lost)+" games. You have drawn " +str(self.Games_Draw)+" games." ,height = 8, width = 30)

    #Function which plays rock paper scissors with user's pick being Scissors
    def Scissors(self):
        UserChoice = 3#Users choice of scissors
        import random
        random_number = random.randint(1,3)#random number generated to pick what choice the computer chooses
        if UserChoice == random_number:#if statement for if computer chose scissors
            self.Game_Number = self.Game_Number+ 1
            self.Games_Draw = self.Games_Draw+ 1#Increases variable value of games drawn
            #message box which gives info on whether you won,lost, or drew the game, number of games, games won, games lost, games drawn
            self.messageBox(title = "Draw", message = "The Computer picked Scissors. You have played a total of "+str(self.Game_Number) +" games. You have won "
                            +str(self.Games_Won)+ " games. You have lost " +str(self.Games_Lost)+" games. You have drawn " +str(self.Games_Draw)+" games.", height = 8, width = 30)
        elif UserChoice == 3 and random_number==2 :
            self.Game_Number = self.Game_Number+ 1
            self.Games_Won = self.Games_Won+ 1#Increases variable value of games won
            self.messageBox(title = "You Win", message = "The Computer picked Paper. You have played a total of "+str(self.Game_Number) +" games. You have won "
                            +str(self.Games_Won)+ " games. You have lost " +str(self.Games_Lost)+" games. You have drawn " +str(self.Games_Draw)+" games.", height = 8, width = 30)
        elif UserChoice == 3 and random_number==1 :#if statement for if computer chose rock
            self.Game_Number = self.Game_Number+ 1
            self.Games_Lost =self.Games_Lost+ 1#Increases variable value of games lost
            self.messageBox(title = "You Lose", message = "The Computer picked Rock. You have played a total of "+str(self.Game_Number) +" games. You have won "
                            +str(self.Games_Won)+ " games. You have lost " +str(self.Games_Lost)+" games. You have drawn " +str(self.Games_Draw)+" games." ,height = 8, width = 30)

    #Function which asks for confirmation and then exits the program
    def Quit(self):
        Confirmation = self.prompterBox(title = "", promptString = "Are you sure you want to exit?", inputText = "", fieldWidth = 20)#pop up box with confirmation prompt
        if Confirmation=="yes" or Confirmation== "Yes":#I the user confirms that they want to exit
            exit()#exits program
        elif Confirmation=="no" or Confirmation== "No":#I the user does not want to exit
            return#returns to main function
        else:
             self.messageBox(title = "Error", message = "Please type yes or no" ,height = 8, width = 30)#error for not typing yes or no to prompt
             self.Quit()#returns user to the confirmation prompt

            
        
#function which calls the main function
def main():
    Final().mainloop()

if __name__ =="__main__":
    main()

