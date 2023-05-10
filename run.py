from tkinter import Tk, ttk
import os, threading
from func import daysstat
import asyncio

class GuiTkinter(Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.title("BitStat")
        self.geometry("200x300")
        self.resizable(False, False)
        
        ttk.Button(self, text='Показать статистику', 
                   command=None
                   ).grid(column=1, row=1)
        
        ttk.Button(self, text='Скачать отчёт 24 часа',
                   command=self.createThreadDownloadInfo
                   ).grid(column=1, row=2)
        
        ttk.Button(self, text='Закрыть',
                   command=self.destroy
                   ).grid(column=1, row=4)

    def createThreadDownloadInfo(self):
        threading.Thread(target=daysstat.download_stat).start()


if __name__ in '__main__':
    app = GuiTkinter().mainloop()
