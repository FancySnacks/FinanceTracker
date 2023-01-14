import customtkinter

from entry import TrackerEntry
from SortButton import SortButton

class EntryListBox:
    def __init__(self, master: customtkinter, parent, root: customtkinter.CTk, row: int = 0, column: int = 0):
        '''
        Args:
             master::customtkinter
                Parent widget element
            parent::Any Object
                The parent object this list belongs to
        '''

        self.master: customtkinter = master
        self.parent = parent
        self.root: customtkinter.CTk = root
        self.row: int = row
        self.column: int = column

        self.entries: list[TrackerEntry] = []


        # ---- Widget ---- #

        self.MainFrame = customtkinter.CTkFrame(master=self.master)
        #self.MainFrame.grid(row=self.row, column=self.column, padx=5, pady=5, sticky="nsew")
        self.MainFrame.pack(expand=True, fill="x", side="left")


        self.TopBar = customtkinter.CTkFrame(master=self.MainFrame, fg_color="transparent")
        self.TopBar.pack(expand=True, fill="x")

        self.TopLabel = customtkinter.CTkLabel(master=self.TopBar,
                                               text="Recent Entries",
                                               font=(("Lato"), 20, "bold"))
        self.TopLabel.pack(anchor="w", pady=5, padx=5)

        self.WalletButton = SortButton(master=self.TopBar, parent=self, text="Wallet")
        self.NameButton = SortButton(master=self.TopBar, parent=self, text="Name")
        self.TypeButton = SortButton(master=self.TopBar, parent=self, text="Type")
        self.ValueButton = SortButton(master=self.TopBar, parent=self, text="Value")
        self.CategoryButton = SortButton(master=self.TopBar, parent=self, text="Category")
        self.DateButton = SortButton(master=self.TopBar, parent=self, text="Date")