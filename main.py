import customtkinter as ctk


root = ctk.CTk()
root.geometry("600x300")
root.title("Duplicate Remover")

# Frame for scan/rescan/stop scan early btn
main_frm = ctk.CTkFrame(root)
main_frm.pack(padx=5, pady=5)

# Set amount of cols
main_frm.columnconfigure(3, weight=1)

# Frame for progress bar
progress_frm = ctk.CTkFrame(root)
# progress_frm.pack(padx=5, pady=5)

# Frame to display result and action buttons (delete all duplicates-always visible, delete-show when one specific duplicate selected, preserve-keep selected copy of file, beneath buttons: expandable treeview with default file to preserve as items, if expanded show rest of file duplicates)
result_frm = ctk.CTkFrame(root)
# result_frm.pack(padx=5, pady=5)


# Create btn to scan device and place on main frm
scan_btn = ctk.CTkButton(main_frm, text="Scan device")
scan_btn.grid(row=0, column=1)



root.mainloop()
