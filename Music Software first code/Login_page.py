






import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk


# RegisterFrame is a child of tk.Toplevel
class RegisterFrame(tk.Toplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Register")
        self.geometry("300x150+600+250")
        # Create widgets when the frame is initialized
        self.create_widgets()
        
    def create_widgets(self):
        # Create and set the position of username label
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Create and set the position of username entry
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Create and set the position of password label
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Create and set the position of password entry
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Create and set the position of register button
        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Function to register a user
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Show an error if the username or password is only whitespace
        if not username.strip() or not password.strip():
            messagebox.showerror("Wrong", "Password or Username cannot only be space!")
        # Show an error if the username already exists
        elif username in self.master.user_data:
            messagebox.showerror("Error", "This user name already exists!")
        else:
            # Otherwise, add the username and password to the user data
            self.master.user_data[username] = password
            # Save the user data
            self.master.save_user_data()
            messagebox.showinfo("Congratulation", "registered successfully!")
            print(f"fully successed: Username={username}, Password={password}")
            self.destroy()


# LoginFrame is a child of tk.Frame
class LoginFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.grid(row=0, column=0, sticky="nsew")
        
        # Load and display the background image
        self.bg_image = Image.open("assets/background.jpeg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Load and display the center background image
        self.center_image = Image.open("assets/background.jpeg")
        self.center_photo = ImageTk.PhotoImage(self.center_image)

        # Create widgets when the frame is initialized
        self.create_widgets()
        # Load user data when the frame is initialized
        self.load_user_data()

    def create_widgets(self):
        # Load and display the background image
        bg_image = Image.open("assets/background.jpeg")
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.background_label = tk.Label(self, image=self.bg_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a new transparent frame in the center of the window
        self.center_frame = tk.Frame(self, bg="")
        self.center_frame.place(relx=0.5, rely=0.5, anchor='c')

        # Create frames for username, password and buttons
        self.username_frame = tk.Frame(self.center_frame)
        self.username_frame.pack(pady=5)
        self.password_frame = tk.Frame(self.center_frame)
        self.password_frame.pack(pady=5)
        self.buttons_frame = tk.Frame(self.center_frame)
        self.buttons_frame.pack(pady=5)

        # Create and place the username label and entry
        self.username_label = tk.Label(self.username_frame, text="Username:", width=10, anchor='w')
        self.username_label.pack(side="left")
        self.username_entry = tk.Entry(self.username_frame)
        self.username_entry.pack(side="left", fill="x", expand=True)

        # Create and place the password label and entry
        self.password_label = tk.Label(self.password_frame, text="Password:", width=10, anchor='w')
        self.password_label.pack(side="left")
        self.password_entry = tk.Entry(self.password_frame, show="*")
        self.password_entry.pack(side="left", fill="x", expand=True)

        # Create and place the login and register buttons
        self.login_button = ttk.Button(self.buttons_frame, text="Login", command=self.login, width=50, style="TButton")
        self.login_button.pack(pady=20)
        self.register_button = ttk.Button(self.buttons_frame, text="Register", command=self.open_register_window, width=50, style="TButton")
        self.register_button.pack(pady=0)

    def load_user_data(self):
        # Load user data from the json file, if it exists
        try:
            with open("user_data.json", "r") as f:
                self.user_data = json.load(f)
        except FileNotFoundError:
            self.user_data = {}

    def save_user_data(self):
        # Save user data to the json file
        with open("user_data.json", "w") as f:
            json.dump(self.user_data, f)

    def login(self):
        # Get username and password input
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Show an error if the username or password is only whitespace
        if not username.strip() or not password.strip():
            messagebox.showerror("Error", "Account or Password!")
        else:
            # Show a success message if the login is correct, otherwise show an error
            if username in self.user_data and self.user_data[username] == password:
                messagebox.showinfo("Congratulation", "Login succeed")
                print(f"Login successfully: Username={username}, Password={password}")
            else:
                messagebox.showerror("Error", "Incorrect Account or Password!")

    def open_register_window(self):
        # Open the RegisterFrame
        RegisterFrame(self)


if __name__ == '__main__':
    # Create the root Tk object, set the size, and make it responsive to window resizing
    root = tk.Tk()
    root.geometry("900x600+300+125")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    # Instantiate the LoginFrame
    app = LoginFrame(master=root)
    # Start the Tkinter event loop
    app.mainloop()



