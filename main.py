# 1. Bring the Tkinter toolbox into our file and give it a short nickname 'tk'
import tkinter as tk
from tkinter import simpledialog, messagebox
import pandas as pd
from cryptography.fernet import Fernet
# Load the master key
with open(".secret.key", "rb") as key_file:
    master_key = key_file.read()

# Create the cipher tool using that key
cipher_suite = Fernet(master_key)

# 2. Create the main, blank window (this is the foundation of the app)
window = tk.Tk()
view_window = None

# 3. Give the window a title at the very top
window.title("Dream Journal")

# 4. Set the starting size of the window (Width x Height)
window.geometry("500x500")

############## DREAM FUNCTIONS #####################

def save_dream():
    dream_text = journal_input.get("1.0", tk.END)
    journal_input.delete("1.0",  tk.END)

    with open("dream.txt", "a") as file:
        if is_lucid.get():
            dream_text += "\n[#LUCID]"
            is_lucid.set(False)

        text_bytes = dream_text.encode("utf-8")
        scrambled_bytes = cipher_suite.encrypt(text_bytes)
        final_text = scrambled_bytes.decode("utf-8")
        file.write(final_text + "\n---\n")

def read_dreams():
    global view_window
    # 1. Ask for the password (the show="*" hides the text as they type)
    user_guess = simpledialog.askstring("Security Check", "Enter Master PIN to unlock:", show="*")

    # 2. Check the password
    if user_guess != "Alcoholic":
        messagebox.showerror("Access Denied", "Intruder alert. Incorrect PIN.")
        return  # This completely stops the function and kicks them out

    full_history = ""
    dream_data = []
    with open("dream.txt", "r") as file:
        # Read the whole file and split it into a list everywhere it sees your separator
        all_dreams = file.read().split("\n---\n")
        for chunk in all_dreams:
            if chunk !="":
                raw_bytes = chunk.encode("utf-8")
                decoded_bytes = cipher_suite.decrypt(raw_bytes)
                readable_text = decoded_bytes.decode("utf-8")
                full_history += readable_text + "\n--------------------\n"
                was_lucid = "[#LUCID]" in readable_text
                dream_data.append({"Dream" : readable_text, "Lucid": was_lucid})
    df = pd.DataFrame(dream_data)
    total_dreams = len(df)
    lucid_count = df["Lucid"].sum()
    if total_dreams > 0:
        success_rate = (lucid_count / total_dreams) * 100
    else:
        success_rate = 0

# Create the pop-up
    if view_window is not None and view_window.winfo_exists():
        view_window.destroy()
    view_window = tk.Toplevel(window)
    view_window.title("Past Dreams Vault")
    view_window.geometry("500x500")
    stats_text = f"Total Dreams: {total_dreams} | Lucid Success Rate: {success_rate:.1f}%"
    stats_label = tk.Label(view_window, text=stats_text, font=("Arial", 12, "bold"))
    stats_label.pack(pady=10)

    display_box = tk.Text(view_window)
    display_box.insert("1.0", full_history)
    display_box.pack()

#####################################################


################## USER INTERFACE ###################
######## MAIN WINDOW ########
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
#############################
######################################################

# 5. Tell the window to stay open in an infinite loop and wait for the user
window.mainloop()