import tkinter as tk

LOCKED = 0
EDIT = 1

NR_OF_COLUMNS = 5

class GUI:
    def __init__(self):
        self.current_naam = "Senne"
        self.current_beschrijving = "Leefweek"
        self.set_up_visuals()

    def set_up_visuals(self):
        self.window = tk.Tk()
        self.window.title("TransactionsToExcel")
        self.window.geometry("1200x800")
        def on_closing():
            self.aborted[0] = True
            self.window.destroy()
        self.window.protocol("WM_DELETE_WINDOW", on_closing)

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=2)
        self.window.rowconfigure(1, weight=4)

        frm_information = tk.Frame(master=self.window)
        frm_information.grid(row=0, column=0, sticky='NSEW')

        frm_information.columnconfigure(0, weight=10)
        frm_information.columnconfigure(1, weight=1)
        frm_information.rowconfigure(0, weight=1)
        frm_information.rowconfigure(1, weight=1)
        frm_information.rowconfigure(2, weight=3)
        frm_information.rowconfigure(3, weight=3)

        #Setting up information label

        self.lbl_date = tk.Label(master=frm_information, text="", font=("Arial",20))
        self.lbl_date.grid(row=0, column=0, padx=5, sticky="W")
        self.lbl_bedrag = tk.Label(master=frm_information, text="", font=("Arial",20))
        self.lbl_bedrag.grid(row=1, column=0, padx=5, sticky="W")

        #Setting up naam
        self.naam_state = LOCKED

        self.lbl_naam = tk.Label(master=frm_information, text=self.current_naam, font=("Arial",25))
        self.lbl_naam.grid(row=2, column=0, padx=5, sticky="W")

        self.ent_naam = tk.Entry(master=frm_information, font=("Arial",25))

        self.btn_naam = tk.Button(master=frm_information, text="Edit", command= self.edit_Naam, font=("Arial",18), padx=50)
        self.btn_naam.grid(row=2, column=1, padx=20, sticky="E")


        #Setting up beschrijving
        self.beschrijving_state = LOCKED

        self.ent_beschrijving = tk.Entry(master=frm_information, font=("Arial",25))

        self.lbl_beschrijving = tk.Label(master=frm_information, text=self.current_beschrijving, font=("Arial",25))
        self.lbl_beschrijving.grid(row=3, column=0, padx=5, sticky="W")

        self.btn_beschrijving = tk.Button(master=frm_information, text="Edit", command= self.edit_Beschrijving, font=("Arial",18), padx=50)
        self.btn_beschrijving.grid(row=3, column=1, padx=20, sticky="E")




        #Setting up the scrollable window
        container = tk.Frame(master=self.window)
        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        container.grid(row=1, column=0, sticky='NSEW')
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def run(self, sheetnames, transactions, aborted):
        self.transactions = transactions
        self.sheetnames = sheetnames
        self.aborted = aborted
        self.initialize_buttons()
        if self.start_process():
            self.window.mainloop()
            
    
    def start_process(self):
        self.id = 0
        while(self.id < len(self.transactions)):
            if self.transactions[self.id][5] == "" or self.transactions[self.id][4] == "" or self.transactions[self.id][3] == "":
                self.show_current_transaction()
                return True
            self.id += 1

    def show_current_transaction(self):
        if self.transactions[self.id][3] == "":
            if self.transactions[self.id][4] == "":
                self.edit_Beschrijving()
                self.edit_Naam()
            else:
                self.edit_Naam()
                self.lbl_beschrijving['text'] = self.transactions[self.id][4]
        else:
            if self.transactions[self.id][4] == "":
                self.edit_Beschrijving()
                self.lbl_naam['text'] = self.transactions[self.id][3]
            else:
                self.lbl_naam['text'] = self.transactions[self.id][3]
                self.lbl_beschrijving['text'] = self.transactions[self.id][4]
        self.lbl_date['text'] = self.transactions[self.id][0]
        self.lbl_bedrag['text'] =  "€ " + self.transactions[self.id][1]
        if float(self.transactions[self.id][1]) > 0:
            self.lbl_bedrag['foreground'] = "green"
        elif float(self.transactions[self.id][1]) < 0:
            self.lbl_bedrag['foreground'] = "red"
        else:
            self.lbl_bedrag['foreground'] = "black"
        

        


    def edit_Naam(self):
        if self.naam_state == LOCKED:
            self.lbl_naam.grid_forget()
            self.ent_naam.delete(0,tk.END)
            self.ent_naam.insert(0, self.transactions[self.id][3])
            self.ent_naam.grid(row=2, column=0, padx=5, sticky="EW")
            self.btn_naam['text'] = "Save"
            self.naam_state = EDIT
            self.naam_beschr_check()
        else:
            self.ent_naam.grid_forget()
            self.transactions[self.id][3] = self.ent_naam.get()
            self.lbl_naam['text'] = self.transactions[self.id][3]
            self.lbl_naam.grid(row=2, column=0, padx=5, sticky="W")
            self.btn_naam['text'] = "Edit"
            self.naam_state = LOCKED
            self.naam_beschr_check()


    def edit_Beschrijving(self):
        if self.beschrijving_state == LOCKED:
            self.lbl_beschrijving.grid_forget()
            self.ent_beschrijving.delete(0,tk.END)
            self.ent_beschrijving.insert(0, self.transactions[self.id][4])
            self.ent_beschrijving.grid(row=3, column=0, padx=5, sticky="EW")
            self.btn_beschrijving['text'] = "Save"
            self.beschrijving_state = EDIT
            self.naam_beschr_check()
        else:
            self.ent_beschrijving.grid_forget()
            self.transactions[self.id][4] = self.ent_beschrijving.get()
            self.lbl_beschrijving['text'] = self.transactions[self.id][4]
            self.lbl_beschrijving.grid(row=3, column=0, padx=5, sticky="W")
            self.btn_beschrijving['text'] = "Edit"
            self.beschrijving_state = LOCKED
            self.naam_beschr_check()
            

    def click_worksheet(self, id):
        self.transactions[self.id][3] = self.lbl_naam['text']
        self.transactions[self.id][4] = self.lbl_beschrijving['text']
        self.transactions[self.id][5] = self.sheetnames[id]
        while(self.id < len(self.transactions)):
            if self.transactions[self.id][5] == "" or self.transactions[self.id][4] == "" or self.transactions[self.id][3] == "":
                self.show_current_transaction()
                return
            self.id += 1
        self.window.destroy()

    
    def initialize_buttons(self):
        self.buttons =[]
        row = 0
        column = 0
        self.scrollable_frame.rowconfigure(0, weight=1)
        for sheetname_nr in range(len(self.sheetnames)):
            
            self.buttons.append(tk.Button(master=self.scrollable_frame, text=self.sheetnames[sheetname_nr][0:18], command= lambda var1 = sheetname_nr :self.click_worksheet(var1), font=("Arial",15), width=18, ))
            self.buttons[sheetname_nr].grid(row= row, column=column, padx=14, pady=7)


            column += 1
            if column == NR_OF_COLUMNS:
                column = 0
                row += 1
    
    def naam_beschr_check(self):
        if self.transactions[self.id][3] == "" or self.transactions[self.id][4] == "" or self.naam_state == EDIT or self.beschrijving_state == EDIT:
            for button in self.buttons:
                button['state'] = tk.DISABLED
        else:
            for button in self.buttons:
                button['state'] = tk.NORMAL
        
    

#Code for testing
# sheetnames = ["Inschrijvingen Inschrijvingen Inschrijvingen", "BBQ", "Leefweek", "Allerlei", "Leidingsweekend 1", "Pannekoeken verkoop"]
# gui = GUI()
# gui.run(sheetnames*5)