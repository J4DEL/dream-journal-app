# 1. Bring the Tkinter toolbox into our file and give it a short nickname 'tk'
import tkinter as tk
import base64

# 2. Create the main, blank window (this is the foundation of the app)
window = tk.Tk()

# 3. Give the window a title at the very top
window.title("Dream Journal")

# 4. Set the starting size of the window (Width x Height)
window.geometry("500x500")

############## DREAM FUNCTIONS #####################

def save_dream():
    dream_text = journal_input.get("1.0", tk.END)

    print("Dream entry successful.")
    journal_input.delete("1.0",  tk.END)

    with open("dream.txt", "a") as file:
        if is_lucid.get():
            dream_text += "\n[#LUCID]"
            is_lucid.set(False)
            text_bytes = dream_text.encode("utf-8")
            scrambled_bytes = base64.b64encode(text_bytes)
            final_text = scrambled_bytes.decode("utf-8")
        file.write(final_text + "\n---\n")

def read_dreams():
    with open("dream.txt", "r") as file:
        # Read the whole file and split it into a list everywhere it sees your separator
        all_dreams = file.read().split("\n---\n")
        for chunk in all_dreams:
            if chunk !="":
                raw_bytes = chunk.encode("utf-8")
                decoded_bytes = base64.b64decode(raw_bytes)
                readable_text = decoded_bytes.decode("utf-8")
                print(readable_text)
                print("-------------------")

#####################################################


################## USER INTERFACE ###################

#text box
journal_input = tk.Text(window)
journal_input.pack()

#lucid dream check box
is_lucid = tk.BooleanVar()
lucid_check = tk.Checkbutton(window, text="Lucid Dream?", variable=is_lucid)
lucid_check.pack()

#save button
save_button = tk.Button(window, text="Save Dream", command=save_dream)
save_button.pack()

#read button
read_button = tk.Button(window, text="Read Past Dreams", command=read_dreams)
read_button.pack()

######################################################

# 5. Tell the window to stay open in an infinite loop and wait for the user
window.mainloop()