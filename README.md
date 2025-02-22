Below is the entire code for LiteSlate.  You can review it and see there is nothing malicious about it.   Without a signature microsoft will always flag EXE's.  




from tkinter import Tk, Label, Entry, Button, Text, messagebox, Checkbutton, IntVar, filedialog
import os
from datetime import datetime

def open_url(url):
    """ Opens a URL in the default web browser """
    import webbrowser  # Lazy import
    webbrowser.open(url)

def get_user_data_directory():
    return os.getenv("APPDATA")  # Or another suitable directory

class LiteSlateApp:
    def __init__(self):
        try:
            self.save_folder = self.get_last_save_folder()
            self.ensure_save_folder_exists()
            self.autosave_interval = 1000
            self.initialize_main_window()
        except Exception as e:
            print(f"Initialization Error: {e}")

    def get_last_save_folder(self):
        last_folder_file = os.path.join(get_user_data_directory(), "last_folder.txt")
        try:
            with open(last_folder_file, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    def ensure_save_folder_exists(self):
        if not self.save_folder:
            messagebox.showinfo("Save Folder Required", "Please choose a save folder before starting.")
            self.set_save_folder()

        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
            with open('last_folder.txt', 'w') as f:
                f.write(self.save_folder)

    def initialize_main_window(self):
        try:
            self.root = Tk()
            self.root.title("LiteSlate")
            
            # Set the desired fixed window size
            window_width = 300
            window_height = 220

            # Get the screen width and height
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            # Calculate the x and y position to center the window
            x = (screen_width // 2) - (window_width // 2)
            y = (screen_height // 2) - (window_height // 2)

            # Set the window size and position
            self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
            self.root.configure(bg="white")

            self.dark_mode_var = IntVar(value=0)
            Label(self.root, text="LiteSlate", font=("Courier", 24), bg="white").pack(pady=20)

            Checkbutton(self.root, text="Enable Dark Mode", variable=self.dark_mode_var, bg="white").pack()
            Button(self.root, text="Change Save Folder", command=self.set_save_folder).pack(pady=5)
            Button(self.root, text="Start Writing", command=self.start_focused_mode).pack(pady=10)

            link1 = Label(self.root, text="Upgrade to TypeSlate", fg="blue", cursor="hand2", bg="white")
            link1.pack(side="bottom", pady=5)
            link1.bind("<Button-1>", lambda e: open_url("https://typeslate.com"))
            
            self.root.mainloop()
        except Exception as e:
            print(f"Main Window Initialization Error: {e}")

    def set_save_folder(self):
        try:
            folder_selected = filedialog.askdirectory(title="Select Save Folder")
            if folder_selected:
                self.save_folder = folder_selected
                last_folder_file = os.path.join(get_user_data_directory(), "last_folder.txt")
                with open(last_folder_file, 'w') as f:
                    f.write(self.save_folder)
        except Exception as e:
            print(f"Set Save Folder Error: {e}")

    def start_focused_mode(self):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.filename = os.path.join(self.save_folder, f"TypeSlate_Autosave_{timestamp}.txt")
            self.activate_fullscreen_mode()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            print(f"Start Focused Mode Error: {e}")

    def activate_fullscreen_mode(self):
        try:
            # Hide the main window (the normal window with buttons and labels)
            self.root.destroy()

            # Create a new window for fullscreen mode, so it does not contain any buttons or labels
            self.root = Tk()
            self.root.title("TypeSlate - Writing Mode")

            # Set the window to fullscreen
            self.root.attributes('-fullscreen', True)
            self.root.overrideredirect(True)  # Remove title bar and borders

            # Set the background color (black for dark mode, white for light mode)
            bg_color = "black" if self.dark_mode_var.get() else "white"
            self.root.configure(bg=bg_color)

            # Create the text area to fill the entire screen
            self.text_area = Text(self.root, font=("Courier", 18), bg=bg_color, 
                                  fg="white" if self.dark_mode_var.get() else "black", wrap="word", insertbackground="black" if not self.dark_mode_var.get() else "white")
            self.text_area.pack(expand=True, fill="both", padx=0, pady=0)

            # Ensure the text area gets focus for typing
            self.text_area.focus_set()

            # Start autosaving and other components
            self.start_autosave()
            self.start_time = datetime.now()

            # Bind the ESC key to confirm whether the user wants to end the session
            self.root.bind('<Escape>', self.handle_escape)

            # Show the window after it was withdrawn
            self.root.deiconify()
            self.root.focus_set()  # Focus on the root window

        except Exception as e:
            print(f"Fullscreen Mode Error: {e}")




    def start_autosave(self):
        try:
            def autosave_action():
                with open(self.filename, "w") as file:
                    file.write(self.text_area.get("1.0", "end-1c"))
                self.root.after(self.autosave_interval, autosave_action)

            autosave_action()
        except Exception as e:
            print(f"Autosave Error: {e}")

    def handle_escape(self, event=None):
        # Ask for confirmation when the user presses Escape
        response = messagebox.askyesno(
            "Finish Session",
            "Are you sure you want to finish your session?"
        )
        if response:  # If the user confirms, finalize the session
            
            self.return_to_main_menu()  # Ensure it goes back to the main menu
        else:
            return  # Allow the user to continue writing

    def return_to_main_menu(self):
        try:
            # Destroy the fullscreen window completely
            self.root.destroy()

            # Reinitialize the main menu (which will create a new window)
            self.initialize_main_window()  # This will recreate the main window with buttons, etc.
        except Exception as e:
            print(f"Return to Main Menu Error: {e}")

if __name__ == "__main__":
    LiteSlateApp()
