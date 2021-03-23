import tkinter as tk

# name = input("Input your name here: ")
# age = input("Input your age here: ")
# location = input("Input your location here: ")
# anim = input("Input your favourite animal here: ")

root = tk.Tk()
root.geometry("400x240")

def getTextInput():
    result=textExample.get("1.0","end")
    print(result)

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="print", 
                    command=getTextInput)

btnRead.pack()

root.mainloop()