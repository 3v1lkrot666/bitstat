from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from func import daysstat
import asyncio
def main():
    test_path = os.path.basename(__file__)
    path = os.path.abspath(__file__).replace(test_path, '')
    root = Tk()
    root.geometry('200x300')
    root.resizable(width=0, height=0)
    ttk.Button(root, text="24 часа", command=daysstat.download_days_stat).place(x=100, y=10)
    ttk.Button(root, text="30 дней", command=None).place(x=100, y=40)
    ttk.Button(root, text="Выйти", command=root.destroy).place(x=100, y=70)
    root.mainloop()

if __name__ in '__main__':
    main()
