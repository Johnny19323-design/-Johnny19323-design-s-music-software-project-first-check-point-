import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from Login_page import RegisterFrame
from Login_page import LoginFrame
from tkinter import PhotoImage, END, CENTER
import json


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # set initial size of window
        self.geometry("900x600")  
        # make the row expandable 
        self.grid_rowconfigure(0, weight=1) 
        # make the column expandable 
        self.grid_columnconfigure(0, weight=1)
        # load the user data from JSON file  
        self.user_data = self.load_user_data() 
        # initial current frame is none 
        self._frame = None  
        # display HomePage as initial page
        self.switch_frame(HomePage) 
        
    # Function to load user data from a JSON file
    def load_user_data(self):
        try:
            with open('user_data.json', 'r') as f:
                return json.load(f)
        # if the file does not exist, return an empty dictionary
        except FileNotFoundError:  
            return {}
    
    # Function to save user data into a JSON file
    def save_user_data(self):
        with open('user_data.json', 'w') as f:
            json.dump(self.user_data, f)

    # Function to switch from current frame to a new frame
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            # destroy the current frame
            self._frame.destroy()  
        self._frame = new_frame
        # display the new frame
        self._frame.grid() 
        # update the GUI 
        self.update_idletasks()  

# HomePage frame class
class HomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # organize widgets in grid style
        self.grid()
        # create the widgets on HomePage  
        self.create_widgets()  
        # set the geometry of the window
        self.master.geometry("900x600+300+50") 

    # Function to create widgets for the home page
    def create_widgets(self):
        # Display the logo
        self.logo_image = PhotoImage(file='assets/logo.png')
        self.logo_label = tk.Label(self, image=self.logo_image)
        self.logo_label.pack(pady=20)

        # Display welcome message
        self.welcome_label = tk.Label(self, text="Welcome to my Adudio player\nPlease Login To Your Account", font=("Arial", 25))
        self.welcome_label.pack(pady=20)
        
        # Create a font
        my_font = font.Font(size=20)
        
        # Define the style for button
        style = ttk.Style()
        style.configure("TButton", font=my_font)

        # Register button
        self.register_button = ttk.Button(self, text="Register", command=self.open_register_window, style="TButton")
        self.register_button.pack(side="left", padx=50, pady=30)

        # Login button
        self.login_button = ttk.Button(self, text="Login", command=self.open_login_window, style="TButton")
        self.login_button.pack(side="right", padx=50, pady=30)

    # Function to open register window when 'Register' button is clicked
    def open_register_window(self):
        self.register_frame = RegisterFrame()
        # make register frame modal
        self.register_frame.grab_set()  

    # Function to save user info
    def save_user_info(self):
        # Get the user information from the input fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Create a dictionary with the user information
        user_info = {
            'username': username,
            'password': password,
        }

        # Open the JSON file and load the existing data
        with open('user_data.json', 'r') as f:
            data = json.load(f)

        # Check if the username already exists in the data
        if username in data:
            messagebox.showerror("Registration Error", "Username already exists.")  # Show error message if username already exists
            return

        # Add the new user information to the data
        data[username] = user_info

        # Write the updated data back to the JSON file
        with open('user_data.json', 'w') as f:
            json.dump(data, f)  # save user info into JSON file

    # Function to open login window when 'Login' button is clicked
    def open_login_window(self):
        # Switch to LoginFrame
        self.master.switch_frame(LoginFrame)  
        self.master.update()
        # update window geometry after switching to LoginFrame  
        self.master.after(0, self.master.geometry, "900x600+300+100")

# Main function to run the program
if __name__ == '__main__':
    # create MainApp instance
    app = MainApp()
    # start the application
    app.mainloop()

