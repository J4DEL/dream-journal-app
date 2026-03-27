# 1. Bring the Tkinter toolbox into our file and give it a short nickname 'tk'
import tkinter as tk

# 2. Create the main, blank window (this is the foundation of the app)
window = tk.Tk()

# 3. Give the window a title at the very top
window.title("MADJS Dream Journal")

# 4. Set the starting size of the window (Width x Height)
window.geometry("500x400")

# 5. Tell the window to stay open in an infinite loop and wait for the user
window.mainloop()