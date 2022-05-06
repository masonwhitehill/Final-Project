from Functions import *
from tkinter import *
days = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14','15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
BC_or_AD = ('AD', 'BC')
class GUI:

    def __init__(self, window):
        self.window = window

        self.frame_left = Frame(self.window)
        self.months = StringVar(value=month_list)
        self.month_box = Listbox(self.frame_left, listvariable=self.months, height=1, selectmode='browse')
        self.month_box.pack(side='top', padx=5, pady=10)

        self.frame_middle = Frame(self.window)
        self.day = StringVar(value=days)
        self.days_box = Listbox(self.frame_middle, listvariable=self.day, height=1, selectmode='browse')
        self.days_box.pack(side='top', padx=15, pady=10)

        self.frame_nearright = Frame(self.window)
        year_input = Entry(self.frame_nearright)
        year_input.pack(side='top', padx=20, pady=10)

        self.frame_right = Frame(self.window)
        self.time = StringVar(value=BC_or_AD)
        self.timebox = Listbox(self.frame_right, listvariable=self.time, height=1, selectmode='browse')
        self.timebox.pack(side='top', padx=25, pady=10)

        self.frame_bottom = Frame(self.window)
        self.button = Button(self.frame_bottom, text='SUBMIT', command=self.clicked)
        self.button.pack(side='bottom', pady=5)

        self.frame_label = Frame(self.window)
        self.output_label = Label(self.frame_label, text='')
        self.output_label.pack(pady=10)


    def clicked(self):
        year = self.year_input.get()
        month = self.month_box.get()
        day = int(self.days_box.get())
        time = self.timebox.get()
        p = finalouptut(year, month, day, time)
        self.output_label.config(text=f'{p}')



