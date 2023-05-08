import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
       
        
        self.entry = tk.Entry(master, width=20, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        # Create buttons
        buttons = [
            '9', '8', '7', '6',
            '5', '4', '3', '2','1',
            'C', '0', '=', '←',
            '+', '-', '*', '/', '%'  
        ]

        
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.handle_click(x)
            tk.Button(master, text=button, width=5, height=2, bg='skyblue', fg='black', command=command).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1
            
                    
        image = tk.PhotoImage(file="")
        image_label = tk.Label(master, image=image)
        image_label.grid(row=0, column=0)
    def handle_click(self, button):
        if button == '=':
            
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif button == 'C':
            self.entry.delete(0, tk.END)  
        elif button == '←':  
            current_text = self.entry.get()
            self.entry.delete(len(current_text) - 1, tk.END)  
        else:
            
            self.entry.insert(tk.END, button)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
