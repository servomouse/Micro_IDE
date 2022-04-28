from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog


def on_open():
    print(filedialog.askopenfilename(initialdir="/", title="Open file",
                                     filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))


def on_save():
    print(filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                       filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))


def main():
    window = Tk()
    window.title("Micro_IDE")
    window.geometry('400x250')
    """ Menu """
    menubar = Menu(window)

    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Open", command=on_open)
    filemenu.add_command(label="Save", command=on_save)
    filemenu.add_command(label="Exit", command=window.quit)
    window.config(menu=menubar)

    f_top = Frame(window)
    f_bot = Frame(window)
    l1 = Label(f_top, width=7, height=4, bg='yellow', text="1")
    l2 = Label(f_top, width=7, height=4, bg='orange', text="2")
    l3 = Label(f_top, width=7, height=4, bg='lightgreen', text="3")
    l4 = Label(f_top, width=7, height=4, bg='lightblue', text="4")
    f_top.pack(anchor=W)
    f_bot.pack(fill='both', expand=1)
    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack(side=LEFT)
    l4.pack(side=LEFT)
    txt = scrolledtext.ScrolledText(f_bot)
    txt.pack(fill='both', expand=1)
    window.mainloop()


if __name__ == '__main__':
    main()
