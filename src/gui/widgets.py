import tkinter as tk
from tkinter import ttk
def create_progress_bar(parent):
    return ttk.Progressbar(parent,orient='horizontal',length=300)
def status_label(parent):
    lbl=tk.Label(parent,text="Ready")
    lbl.pack()
    return lbl
def cancel_button(parent,cmd):
    btn=tk.Button(parent,text="Cancel",command=cmd)
    return btn
