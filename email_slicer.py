import tkinter as tk

def slice_email():
    email = email_entry.get()
    username, domain = email.split('@')
    result_label.config(text=f"Username: {username}\nDomain: {domain}")

root = tk.Tk() #frame
root.title("Email Slicer")
root.geometry("500x440")
root.resizable(width=False,height=False)
root.config( background='orange')
email_label = tk.Label(root, text="Enter your email address:",width=20,height=1)
email_entry = tk.Entry(root,width=25)
slice_button = tk.Button(root, text="Slice", command=slice_email,bg='black',fg='white',width=10,height=5)
slice_button.place(anchor='center')
result_label = tk.Label(root, text="")
email_label.pack()
email_entry.pack(padx=10,pady=10)
slice_button.pack(padx=100,pady=50)
result_label.pack()
root.mainloop()