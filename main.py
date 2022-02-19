from time import sleep
import keyboard
import mouse
from tkinter import *

def Autoclicker():

    start_key = StartKeyInput.get()

    stop_key = StopKeyInput.get()

    klick = float(KlickKey.get())

    while True:
        if keyboard.is_pressed(start_key):
            mouse.is_pressed(button = 'left')
            while True:
                sleep(klick)
                mouse.double_click(button = 'left')
                if keyboard.is_pressed(stop_key):
                    break

root = Tk()

root['bg'] = '#292929'
root.title("Автоклікер")
root.geometry('600x400')
root.resizable(width=False, height=False)
root.wm_attributes('-alpha', 0.9)

frame = Frame(root, bg = '#292929')
frame.place(relwidth = 1, relheight = 1)

title1 = Label(frame, text = 'Клавіша запуску: ', fg = 'white', bg = '#292929', font = ('Arvo', 21, 'bold'))
title1.place(x = 40, y = 20)

StartKeyInput = Entry(frame, bg = '#292929', fg = 'white', font = ('Arvo', 15, 'bold'))
StartKeyInput.place(x = 330, y = 27, width = 200, height = 30)
start_key = 'o'

title2 = Label(frame, text = 'Клавіша зупинки: ', fg = 'white', bg = '#292929', font = ('Arvo', 21, 'bold'))
title2.place(x = 40, y = 100)

StopKeyInput = Entry(frame, bg = '#292929', fg = 'white', font = ('Arvo', 15, 'bold'))
StopKeyInput.place(x = 330, y = 106, width = 200, height = 30)
stop_key = 'p'

title3 = Label(frame, text = 'Швидкість кліків(с): ', fg = 'white', bg = '#292929', font = ('Arvo', 21, 'bold'))
title3.place(x = 40, y = 180)

KlickKey = Entry(frame, bg = '#292929', fg = 'white', font = ('Arvo', 15, 'bold'))
KlickKey.place(x = 330, y = 185, width = 200, height = 30)
klickS = 1000

btn = Button(frame, text = 'Налаштувати', fg = 'white', bg = '#292929', font = ('Arvo', 21, 'bold'), command = Autoclicker)
btn.place(x = 200, y = 300, width = 200, height = 50)

root.mainloop()