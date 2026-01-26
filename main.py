import customtkinter as ctk
from tkinter import messagebox
import database

database.create_table()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Modern Login System")
        self.resizable(False, False)
        center_window(self, 420, 480)

        self.frame = ctk.CTkFrame(self, corner_radius=20, fg_color="#1f1f1f")
        self.frame.pack(pady=40, padx=40, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.frame, text="Login", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        self.username = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.username.pack(pady=12, padx=20, fill="x")

        self.password = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.password.pack(pady=12, padx=20, fill="x")

        self.login_btn = ctk.CTkButton(self.frame, text="Login", command=self.login)
        self.login_btn.pack(pady=12, padx=20, fill="x")

        self.register_btn = ctk.CTkButton(self.frame, text="Register", command=self.open_register)
        self.register_btn.pack(pady=12, padx=20, fill="x")

    def login(self):
        username = self.username.get()
        password = self.password.get()

        if database.login_user(username, password):
            messagebox.showinfo("Success", "Logged in successfully!")
            self.open_dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def open_register(self):
        register = ctk.CTkToplevel(self)
        register.title("Register")
        center_window(register, 380, 360)

        # Modal behavior
        register.transient(self)
        register.grab_set()
        register.focus()

        frame = ctk.CTkFrame(register, corner_radius=20)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Create Account", font=("Arial", 20, "bold")).pack(pady=20)

        username = ctk.CTkEntry(frame, placeholder_text="Username")
        username.pack(pady=10, fill="x")

        password = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
        password.pack(pady=10, fill="x")

        def register_user():
            if database.register_user(username.get(), password.get()):
                messagebox.showinfo("Success", "Account created!")
                register.destroy()
            else:
                messagebox.showerror("Error", "Username already exists")

        ctk.CTkButton(frame, text="Register", command=register_user).pack(pady=20, fill="x")

    def open_dashboard(self, username):
        dash = ctk.CTkToplevel(self)
        dash.title("Dashboard")
        center_window(dash, 420, 400)

        # Modal behavior
        dash.transient(self)
        dash.grab_set()
        dash.focus()

        frame = ctk.CTkFrame(dash, corner_radius=20)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text=f"Welcome, {username}", font=("Arial", 22, "bold")).pack(pady=20)

        ctk.CTkButton(frame, text="Profile", command=lambda: self.open_profile(username)).pack(pady=10, fill="x")
        ctk.CTkButton(frame, text="Delete Account", command=lambda: self.delete_account(username)).pack(pady=10, fill="x")
        ctk.CTkButton(frame, text="Logout", command=dash.destroy).pack(pady=10, fill="x")

    def open_profile(self, username):
        profile = ctk.CTkToplevel(self)
        profile.title("Profile")
        center_window(profile, 360, 220)

        # Modal behavior
        profile.transient(self)
        profile.grab_set()
        profile.focus()

        frame = ctk.CTkFrame(profile, corner_radius=20)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Profile", font=("Arial", 22, "bold")).pack(pady=20)
        ctk.CTkLabel(frame, text=f"Username: {username}", font=("Arial", 16)).pack(pady=10)

    def delete_account(self, username):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this account?")
        if confirm:
            if database.delete_user(username, self.password.get()):
                messagebox.showinfo("Deleted", "Account deleted successfully!")
            else:
                messagebox.showerror("Error", "Unable to delete account")


if __name__ == "__main__":
    app = App()
    app.mainloop()
