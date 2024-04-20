import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x500")
root.title('form Login')

def login():
    
    finishLabel.configure(text="ini test xixixixi")

frame = ctk.CTkFrame(master = root)
frame.pack(pady=20,padx=60,fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="login system",)
label.pack(pady=12,padx=10)

finishLabel = ctk.CTkLabel(root, text=" ")
finishLabel.pack()

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)

entry2= ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12,padx=10)

button = ctk.CTkButton(master = frame, text="login", command=login)
button.pack(pady=12 , padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='remember me')
checkbox.pack(pady=12,padx=10)

root.mainloop()
