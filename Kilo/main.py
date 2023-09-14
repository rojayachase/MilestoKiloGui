import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Demo')
window.geometry('300x150')

# title
title_label = ttk.Label(
    master=window, text='Miles to kilometers', font='Calibri 24 bold')
title_label.pack()


def convert():
    print(entry.get())


# input field
input_frame = ttk.Frame(master=window)
entryInt = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entryInt)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_label = ttk.Label(master=window, text='Output', font='Calibri 24')
output_label.pack(padx=5)

# run
window.mainloop()