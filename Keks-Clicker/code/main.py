from values import read, save_values
from archivement import archivements
from function_gui import more_cookies, upgrade
from tkinter import ttk, Tk, N, W, E, S, PhotoImage, StringVar


# create window
class Main:
    """A simple cookie clicker made in python with tkinter"""
    def __init__(self):
        """initializes the window
        and the path to to photo used in the _main_button"""
        self._window = Tk()
        self._window.title("Kekse Clicker")
        self._picture_path = PhotoImage(file=__file__.rsplit("\\", maxsplit=2)[0] + "\\keks.png")
        self._init_vars()
        self._init_window()

    def _init_vars(self):
        """initializes all needed variables"""
        temp = read()
        self.kekse = StringVar(value=str(temp[0]))
        self.upgrades = StringVar(value=str(temp[1]))
        self.multiplicator = StringVar(value=str(temp[2]))
        self.info = StringVar(value="Nichts")
        self.archivement_text = StringVar(value="Nicht neues")

    def _init_window(self):
        """the mainframe,
        _show_coockies and
        the button"""
        mainframe = ttk.Frame(self._window, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self._window.columnconfigure(0, weight=1)
        self._window.rowconfigure(0, weight=1)

        self._show_cookies = ttk.Label(mainframe, width=20, text="Kekse: {0}" .format(self.kekse.get()))
        self._show_cookies.grid(column=1, row=1, sticky=(N, W))

        ttk.Button(mainframe, image=self._picture_path, command=self._main_click).grid(column=2, row=2)

        self._show_multiplicator = ttk.Label(mainframe, width=20, text="Multiplikator: {0}" .format(self.multiplicator.get()))
        self._show_multiplicator.grid(column=1, row=2, sticky=N)

        self.upgrade_button = ttk.Button(mainframe, text="Upgrade price:\n{0}" .format(self.upgrades.get()), command=self._upgrades_click)
        self.upgrade_button.grid(column=3, row=2)

        infobox = ttk.Label(mainframe, width=20, textvariable=self.info)
        infobox.grid(column=1, row=3, sticky=(W, S))

        arch_box = ttk.Label(mainframe, width=30, textvariable=self.archivement_text)
        arch_box.grid(column=3, row=1, sticky=(N, E))

    def _main_click(self):
        """calls more_cookies function and
        updates the text from the _show_cookies label"""
        more_cookies(self.kekse, self.multiplicator)
        self._show_cookies["text"] = "Kekse: {0}".format(str(self.kekse.get()))

        archivements(self.kekse, self.multiplicator, self.archivement_text)

    def _upgrades_click(self):
        upgrade(self.kekse, self.upgrades, self.multiplicator, self.info)
        self._update()

    def _update(self):
        self._show_cookies["text"] = "Kekse: {0}".format(str(self.kekse.get()))
        self._show_multiplicator["text"] = "Multiplikator: {0}" .format(self.multiplicator.get())
        self.upgrade_button["text"] = "Upgrade price:\n{0}" .format(self.upgrades.get())

    def start(self):
        """starts entire programm"""
        self._window.mainloop()
        save_values([self.kekse.get(), self.upgrades.get(), self.multiplicator.get()])


Main().start()
