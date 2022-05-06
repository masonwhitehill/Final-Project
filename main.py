from gui import *

def main():
    window = Tk()
    window.title('Mayan Calendar Calculator')
    window.geometry('300x100')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()