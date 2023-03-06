def my_reset():
    for widget in my_w.winfo_children():
        if isinstance(widget, tk.Entry): # If this is an Entry widget class
            widget.delete(0,'end')   # delete all entries 
        if isinstance(widget,ttk.Combobox):
            widget.delete(0,'end') 
        if isinstance(widget,tk.Text):
            widget.delete('1.0','end') # Delete from position 0 till end 
        if isinstance(widget,tk.Checkbutton):
            widget.deselect()
        if isinstance(widget,tk.Radiobutton):
            my_r.set(None)
