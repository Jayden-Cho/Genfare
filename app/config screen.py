import tkinter as tk

class FilteredListbox(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_widgets()
        
    def create_widgets(self):
        # Create the left listbox
        self.left_lb = tk.Listbox(self)
        self.left_lb.pack(side="left", fill="both", expand=True)
        self.left_lb.bind("<<ListboxSelect>>", self.filter_list)
        
        # Create the middle listbox
        self.middle_lb = tk.Listbox(self)
        self.middle_lb.pack(side="left", fill="both", expand=True)
        
        # Create the right section
        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side="right", fill="both", expand=True)
        
        # Create a scrollbar for the middle listbox
        self.middle_scrollbar = tk.Scrollbar(self.middle_lb)
        self.middle_scrollbar.pack(side="right", fill="y")
        
        # Attach the scrollbar to the middle listbox
        self.middle_lb.config(yscrollcommand=self.middle_scrollbar.set)
        self.middle_scrollbar.config(command=self.middle_lb.yview)
        
    def filter_list(self, event):
        # Get the selected item(s) from the left listbox
        selected_items = self.left_lb.curselection()
        if not selected_items:
            # If nothing is selected, show everything
            self.middle_lb.delete(0, "end")
            self.middle_lb.insert("end", *self.data)
        else:
            # Otherwise, filter the list
            self.middle_lb.delete(0, "end")
            for i in selected_items:
                # actual filter, the filter will have to be a little different since we want different name 
                filter_text = self.left_lb.get(i)
                filtered_items = [item for item in self.data if filter_text in item]
                self.middle_lb.insert("end", *filtered_items)
    
    def set_data(self, left_data, middle_data):
        # Set the data for the listboxes
        self.left_data = left_data
        self.middle_data = middle_data
        self.left_lb.delete(0, "end")
        self.left_lb.insert("end", *sorted(set([item.split()[0] for item in left_data])))
        self.data = middle_data
        self.middle_lb.delete(0, "end")
        self.middle_lb.insert("end", *middle_data)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Genfare Configuration Assistant")
    
    # Create the main frame
    main_frame = tk.Frame(root)
    main_frame.pack(side="top", fill="both", expand=True)
    
    # Create the filtered listbox
    filtered_lb = FilteredListbox(main_frame)
    filtered_lb.pack(side="top", fill="both", expand=True)
    
    # Set the data for the listboxes
    left_data = ["red", "yellow", "green", "orange", "purple"]
    middle_data = ["apple red", "banana yellow", "cherry red", "date brown", "elderberry purple", "fig green",
                   "grape red", "kiwi green", "lemon yellow", "melon green", "orange orange", "pear green",
                   "pineapple yellow", "plum purple", "raspberry red", "strawberry red", "watermelon green"]
    filtered_lb.set_data(left_data, middle_data)
    
    root.mainloop()
