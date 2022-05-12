from Functions import *
from tkinter import *

class GUI:

    def __init__(self, window):
        self.window = window

        self.frame_date = Frame(self.window)
        self.output_date = Label(self.frame_date, text='Date:')
        self.output_date.pack(side='top', padx=1, pady=5)
        self.output_date.pack()
        self.frame_date.pack()

        self.frame_left = Frame(self.window)
        self.months = StringVar(value=month_list)
        self.month_box = Listbox(self.frame_left, listvariable=self.months, width=9, height=1, selectmode='browse')
        self.month_box.pack(side='top', padx=5, pady=5)
        self.frame_left.pack()

        self.frame_middle = Frame(self.window)
        self.day = StringVar(value=date)
        self.days_box = Listbox(self.frame_middle, listvariable=self.day, width=2, height=1, selectmode='browse')
        self.days_box.pack(side='top', padx=7, pady=5)
        self.frame_middle.pack()


        self.frame_nearright = Frame(self.window)
        self.year_input = Entry(self.frame_nearright, width=5)
        self.year_input.pack(side='top', padx=20, pady=5)
        self.frame_nearright.pack()

        self.frame_right = Frame(self.window)
        self.time = StringVar(value=BC_or_AD)
        self.timebox = Listbox(self.frame_right, listvariable=self.time, width=3, height=1, selectmode='browse')
        self.timebox.pack(side='top', padx=25, pady=5)
        self.frame_right.pack()

        self.frame_bottom = Frame(self.window)
        self.button = Button(self.frame_bottom, text='SUBMIT', command=self.clicked)
        self.button.pack(side='bottom', pady=5)
        self.frame_bottom.pack()

        self.frame_mayan = Frame(self.window)
        self.output_mayan = Label(self.frame_mayan, text='Mayan Calender Date:')
        self.output_mayan.pack(pady=10)
        self.output_mayan.pack()
        self.frame_mayan.pack()

        self.frame_label = Frame(self.window)
        self.output_label = Label(self.frame_label, text='')
        self.output_label.pack()
        self.frame_label.pack()


    def clicked(self):
        year = int(self.year_input.get())

        month = str(self.month_box.get(ACTIVE))
        day = int(self.days_box.get(ACTIVE))
        time = str(self.timebox.get(ACTIVE))
        p = final_output(year, month, day, time)
        self.output_label.config(text=f'{p}')

