#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
tic_tac_toe = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

tic_tac_toe_keys = []

for key in tic_tac_toe:
    tic_tac_toe_keys.append(key)



def printBoard(ttt):
    print(ttt['7'] + '|' + ttt['8'] + '|' + ttt['9'])
    print('-+-+-')
    print(ttt['4'] + '|' + ttt['5'] + '|' + ttt['6'])
    print('-+-+-')
    print(ttt['1'] + '|' + ttt['2'] + '|' + ttt['3'])


def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(tic_tac_toe)
        print("It's your turn," + turn + ".Which place do you want the move?")

        move = input()        

        if tic_tac_toe[move] == ' ':
            tic_tac_toe[move] = turn
            count += 1
        else:
            print("That place is already filled.\nRe-enter the place?")
            continue

        win=False 
        if count >= 5:
            
            if tic_tac_toe['7'] == tic_tac_toe['8'] == tic_tac_toe['9'] != ' ': 
                printBoard(tic_tac_toe)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                win=True
                break
            elif tic_tac_toe['4'] == tic_tac_toe['5'] == tic_tac_toe['6'] != ' ': 
                printBoard(tic_tac_toe)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                win=True
                break
            elif tic_tac_toe['1'] == tic_tac_toe['2'] == tic_tac_toe['3'] != ' ': 
                printBoard(tic_tac_toe)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                win=True
                break
            elif tic_tac_toe['1'] == tic_tac_toe['4'] == tic_tac_toe['7'] != ' ': 
                printBoard(tic_tac_toe)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                win=True
                break
            elif tic_tac_toe['2'] == tic_tac_toe['5'] == tic_tac_toe['8'] != ' ': 
                printBoard(tic_tac_toe)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                win=True
                break
            elif tic_tac_toe['3'] == tic_tac_toe['6'] == tic_tac_toe['9'] != ' ': 
                printBoard(tic_tac_toe)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                win=True
                break 
            elif tic_tac_toe['7'] == tic_tac_toe['5'] == tic_tac_toe['3'] != ' ': 
                printBoard(tic_tac_toe)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                win=True
                break
            elif tic_tac_toe['1'] == tic_tac_toe['5'] == tic_tac_toe['9'] != ' ': 
                printBoard(tic_tac_toe)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                win=True
                break 
         

        
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
            root=Tk()
            root.title('Tic Tac Toe')
            root.geometry('350x200')

            label = Label(root , text ="Both are smart. Its a tie!!") 
            label.pack()

            root.mainloop()

        

        
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X' 
            
    if win==True:
        root=Tk()
        root.title('Tic Tac Toe')
        root.geometry('350x200')
        label = Label(root , text ="Hurray!!! You won") 
        label.pack()

        root.mainloop()
    
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in tic_tac_toe_keys:
            tic_tac_toe[key] = " "

        game()

if __name__ == "__main__":
    game()


# In[ ]:




