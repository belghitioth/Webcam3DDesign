
"""
Created on Wed Jun 01 21:57:40 2016

@author: belghitioth
"""



from Tkinter import *

import tkFileDialog
import sys
import os






main = Tk()
main.geometry("500x400+350+400")
main.title("Dessin 3D par Webcam")

def quitter():
    main.destroy()

def dessiner():
    os.system("python dessiner.py")
    
def ouvrir():
    os.system("python visualiser.py")
   

    


label = Label(main, text="Bienvenue dans le Logiciel Dessin 3D ")
label.pack()

# Creation d'un widget Canvas
Canevas = Canvas(main)
Canevas.pack(padx=5,pady=5)

message = Label(main, text="Par Iheb , Othmane, Aymane")

message.pack(side="bottom", fill=Y)



bouton1 = Button(main,command=dessiner, width = 20, height = 5)
bouton1['text'] = 'Commencer l\'experience'
bouton1.place(x='50',y='150')

bouton1 = Button(main,command=ouvrir, width = 20, height = 5)
bouton1['text'] = 'Visualiser fichier    '
bouton1.place(x='250',y='150')


menu = Menu(main)
sousmenu = Menu(menu, tearoff = 0)
menu.add_cascade(label="Menu", menu=sousmenu)
sousmenu.add_command(label="Quitter     ",command=quitter)
menu.add_command(label="Dessiner", command=dessiner)
menu.add_command(label="Visualiser", command=ouvrir)

gifdict={}

main.config(menu = menu)

main.mainloop()
