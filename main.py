import tkinter.messagebox

from subdef import *

def alphabetWindow(option):
    def stop():
        alphabetWindow.destroy()
        mainWindow.deiconify()
    if option != "":
        mainWindow.withdraw()
        alphabetWindow = alphabetsettings(option)
        alphabetWindow.protocol("WM_DELETE_WINDOW", stop)
        alphabetWindow.mainloop()

def mainWindowSet(main):
    for index in range(28):
        row, column, val = index//7, index%7, ascii_uppercase[index] if index < 26 else "All" if index == 26 else ""
        globals()[f"alphabet_button{val}"] = buttonsettings(main, text=val)
        exec(f"alphabet_button{val}.grid(row={row}, column={column})\n"
             f"alphabet_button{val}.configure(command=lambda:alphabetWindow(alphabet_button{val}.cget('text')))")

mainWindow = tk.Tk()
settings(mainWindow, tit="Main Title", rszx=False, rszy=False, w='1301', h='703')
mainWindow.protocol("WM_DELETE_WINDOW", sys.exit)
mainWindowSet(mainWindow)
mainWindow.mainloop()
