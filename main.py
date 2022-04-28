from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from pynput import keyboard
from pynput.keyboard import Key

# here are all the attrebutes of pynput.keyboard.Key
# [   'alt', 'backspace', 'cmd', 'ctrl', 'delete', 'down', 'end', 'enter',
#     'esc', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18',
#     'f19', 'f2', 'f20', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'home',
#     'insert','left', 'menu', 'pause', 'right', 'shift', 'space', 'tab', 'up']


def on_ctrl_press(key):
    if key == Key.ctrl:
        print("Press")
    else:
        print(Key.ctrl)


def on_ctrl_release(key):
    if key == Key.ctrl:
        print("Release")
    else:
        print(Key.ctrl)


def on_open(textfield):
    # print(filedialog.askopenfilename(initialdir="/", title="Open file",
    #                                  filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))
    print(textfield.get(1.0, END))


def on_save():
    print(filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                       filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))


def add_separator(event, textfield):
    print(event)


def main():
    # with keyboard.Listener(on_press=on_ctrl_press, on_release=on_ctrl_release) as listener:
    #     listener.join()

    window = Tk()
    window.title("Micro_IDE")
    window.geometry('400x250')
    """ Menu """
    menubar = Menu(window)

    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    window.config(menu=menubar)

    top_frame = Frame(window)
    bottom_frame = Frame(window)
    l1 = Label(top_frame, width=7, height=4, bg='yellow', text="1")
    l2 = Label(top_frame, width=7, height=4, bg='orange', text="2")
    l3 = Label(top_frame, width=7, height=4, bg='lightgreen', text="3")
    l4 = Label(top_frame, width=7, height=4, bg='lightblue', text="4")
    top_frame.pack(anchor=W)
    bottom_frame.pack(fill='both', expand=1)
    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack(side=LEFT)
    l4.pack(side=LEFT)
    textfield = scrolledtext.ScrolledText(bottom_frame, undo=1)
    textfield.pack(fill='both', expand=1)
    textfield.bind('<KeyRelease>', lambda event: add_separator(event, textfield))

    filemenu.add_command(label="Open", command=lambda: on_open(textfield))
    filemenu.add_command(label="Save", command=on_save)
    filemenu.add_command(label="Exit", command=window.quit)
    window.mainloop()


if __name__ == '__main__':
    main()
