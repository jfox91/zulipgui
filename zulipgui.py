import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime

entries = []

def add_entry():
    ticket = ticket_entry.get()
    comment = comment_entry.get()
    hours = hours_entry.get()

    if not ticket:
        messagebox.showwarning("Input Error", "Ticket number is required.")
        return

    if ticket.lower() == "none":
        ticket_text = "No ticketed work"
    else:
        ticket_text = f"[INFRA2-{ticket}](https://eagleeyenetworks.atlassian.net/browse/INFRA2-{ticket})"

    entries.append((len(entries)+1, ticket_text, comment, hours))
    update_display()

    ticket_entry.delete(0, tk.END)
    comment_entry.delete(0, tk.END)
    hours_entry.delete(0, tk.END)

def update_display():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "| # | Ticket | Comment | Hours |\n")
    output_text.insert(tk.END, "|---|--------|---------|--------|\n")
    for entry in entries:
        output_text.insert(tk.END, f"| {entry[0]} | {entry[1]} | {entry[2]} | {entry[3]} |\n")

def finish():
    date_str = datetime.now().strftime("%Y-%m-%d")
    final = f"My update for {date_str}\n\n"
    final += output_text.get(1.0, tk.END)

    result_window = tk.Toplevel(root)
    result_window.title("Markdown Output")
    text_widget = scrolledtext.ScrolledText(result_window, width=80, height=20)
    text_widget.pack()
    text_widget.insert(tk.END, final)

root = tk.Tk()
root.title("Daily Update GUI")

# Ticket input
tk.Label(root, text="Ticket Number:").grid(row=0, column=0, sticky='e')
ticket_entry = tk.Entry(root)
ticket_entry.grid(row=0, column=1, padx=1, pady=5)

# Comment input
tk.Label(root, text="Comment:").grid(row=1, column=0, sticky='e')
comment_entry = tk.Entry(root)
comment_entry.grid(row=1, column=1, padx=5, pady=5)

# Hours input
tk.Label(root, text="Hours:").grid(row=2, column=0, sticky='e')
hours_entry = tk.Entry(root)
hours_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

finish_button = tk.Button(root, text="Finish and Show Markdown", command=finish)
finish_button.grid(row=4, column=0, columnspan=2, pady=5)

# Output display
output_text = scrolledtext.ScrolledText(root, width=80, height=10)
output_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
