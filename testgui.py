import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

root = tk.Tk()
root.title("Test Layout")

tk.Label(root, text="Ticket Number:").grid(row=0, column=0, sticky='w')
ticket_entry = tk.Entry(root)
ticket_entry.grid(row=0, column=1, sticky="we")

tk.Label(root, text="Comment:").grid(row=1, column=0, sticky='w')
comment_entry = tk.Entry(root)
comment_entry.grid(row=1, column=1, sticky="we")

tk.Label(root, text="Hours:").grid(row=2, column=0, sticky='w')
hours_entry = tk.Entry(root)
hours_entry.grid(row=2, column=1, sticky="we")

add_button = tk.Button(root, text="Add Entry")
add_button.grid(row=3, column=0, columnspan=2)

finish_button = tk.Button(root, text="Finish")
finish_button.grid(row=4, column=0, columnspan=2)

output_text = scrolledtext.ScrolledText(root, width=80, height=10)
output_text.grid(row=5, column=0, columnspan=2, sticky="nsew")

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(5, weight=1)

root.mainloop()
