# main.py
from interface import Game
from tkinter import Tk
import pygame


root = None  # Добавьте эту строку

def main():
    global root  # Добавьте эту строку
    root = Tk()
    game = Game(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)  # Добавьте эту строку
    #root.mainloop()

def on_closing():
    pygame.mixer.music.stop()  # Остановите музыку перед закрытием окна
    pygame.quit()  # Добавьте эту строку
    root.destroy()

if __name__ == "__main__":
    main()
