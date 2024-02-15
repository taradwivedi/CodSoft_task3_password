# Task 3
# Password Generator
import tkinter as tk
import random
import string

# Creation of root window
root = tk.Tk()

# Window title
root.title("Password Generator")
    

def genpass_function():
        
    try:
        # Get password length
        pass_len = int(length_entry.get())

        # To check for validity
        if pass_len  <= 0:
            passgen_lbl.config(text="Invalid Entry")
            return
        

        # Get choice of complexity
        cmplx = v.get()
        
        # Password will be generated based on complexity
        password = rnd_pass(pass_len,cmplx)        

        # Generated password is displayed
        passgen_lbl.config(text=f"Password: {password}")

    except Exception as e:
        passgen_lbl.config(text=f"Error: {e}")

def rnd_pass(length,cmplx):
    # Concatenate characters depending on complexity
    if cmplx == 1:
        pass_char = string.digits + string.ascii_letters + string.punctuation
    elif cmplx == 2:
        pass_char = string.digits + string.ascii_letters 
    elif cmplx == 3:
        pass_char = string.ascii_letters 
    else:
        raise ValueError("Invalid Selction")

    return ''.join(random.choice(pass_char) for _ in range(length))
    

v = tk.IntVar()
# Initial choice set at "strong"
v.set(1)  

# Creating frame 
frame = tk.Frame()
frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S) 

# Adding widgets to frame 
label2 = tk.Label(frame, text="Password Length:")
label2.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

length_entry = tk.Entry(frame, width=10)
length_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

passcomplx_lbl = tk.Label(frame, text="Password Mode:")
passcomplx_lbl.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

# Creating frame 1
frame1 = tk.Frame()
frame1.grid(row=2, column=0, sticky=tk.W+tk.E+tk.N+tk.S) 

# Adding widgets to frame 1
R1 = tk.Radiobutton(frame1, text="Strong", variable=v, value=1)
R1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
R2 = tk.Radiobutton(frame1, text="Weak", variable=v, value=2)
R2.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
R3 = tk.Radiobutton(frame1, text="Poor", variable=v, value=3)
R3.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)



# Create password button
passgen_btn = tk.Button(root, text="Create Password",fg="red", command= genpass_function)
passgen_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Display the created password
passgen_lbl = tk.Label(root, text="",fg="red")
passgen_lbl.grid(row=4, column=0, columnspan=2, padx=10, pady=10)




# Sets cursor at the entry label
length_entry.focus_set()
root.mainloop() 