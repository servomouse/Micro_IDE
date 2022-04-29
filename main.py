from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from pynput import keyboard
from pynput.keyboard import Key
import platform


def on_window_closing(window):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

# here are all the attrebutes of pynput.keyboard.Key
# [   'alt', 'backspace', 'cmd', 'ctrl', 'delete', 'down', 'end', 'enter',
#     'esc', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18',
#     'f19', 'f2', 'f20', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'home',
#     'insert','left', 'menu', 'pause', 'right', 'shift', 'space', 'tab', 'up']


def on_ctrl_press(key):
    pass
    # if key == Key.ctrl:
    #     print("Press")
    # else:
    #     print(Key.ctrl)


def on_ctrl_release(key):
    pass
    # if key == Key.ctrl:
    #     print("Release")
    # else:
    #     print(Key.ctrl)


def on_open(textfield):
    filepath = filedialog.askopenfilename(initialdir="/", title="Open file",
                                          filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*")))
    if filepath != ():
        with open(filepath) as outfile:
            textfield.insert(INSERT, outfile.read())


def on_save(textfield):
    filepath = filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                            filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*")))
    if filepath != ():
        with open(filepath, 'w') as outfile:
            outfile.write(textfield.get(1.0, END))


def add_separator(event, textfield):
    print(event)


def main():
    # with keyboard.Listener(on_press=on_ctrl_press, on_release=on_ctrl_release) as listener:
    #     listener.join()
    current_os = platform.system()

    window = Tk()
    window.title("Micro_IDE")
    window.geometry('900x480')
    if current_os == "Linux":
        window.attributes('-zoomed', True)
    else:
        window.attributes('-fullscreen', True)
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
    filemenu.add_command(label="Save", command=lambda: on_save(textfield))
    filemenu.add_command(label="Exit", command=window.quit)

    window.protocol("WM_DELETE_WINDOW", lambda: on_window_closing(window))
    window.mainloop()


if __name__ == '__main__':
    main()
