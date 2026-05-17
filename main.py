import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("600x300")
root.title("Duplicate Remover")

# Frame for scan/rescan/stop scan early btn
main_frm = ttk.Frame()
main_frm.pack(padx=5, pady=5)

# Set amount of cols
main_frm.columnconfigure(3, weight=1)

# Frame for progress bar
progress_frm = ttk.Frame()
progress_frm.pack(padx=5, pady=5)

# Frame to display result and action buttons (delete all duplicates-always visible, delete-show when one specific duplicate selected, preserve-keep selected copy of file, beneath buttons: expandable treeview with default file to preserve as items, if expanded show rest of file duplicates)
result_frm = ttk.Frame()
result_frm.pack(padx=5, pady=5)


# Create btn to scan device and place on main frm
scan_btn = ttk.Button(main_frm, text="Scan device")
scan_btn.grid(row=0, column=1)



root.mainloop()
