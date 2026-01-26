import tkinter as tk
from tkinter import ttk, messagebox
import database

database.create_table()


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


# ---------- Register Window ----------
def open_register_window():
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.resizable(False, False)
    center_window(register_window, 360, 280)

    # Frame
    frame = ttk.Frame(register_window, padding=20)
    frame.pack(expand=True, fill="both")

    ttk.Label(frame, text="Create a New Account", font=("Arial", 14, "bold")).pack(pady=10)

    ttk.Label(frame, text="Username:").pack(anchor="w", pady=5)
    reg_username = ttk.Entry(frame)
    reg_username.pack(fill="x")

    ttk.Label(frame, text="Password:").pack(anchor="w", pady=5)
    reg_password = ttk.Entry(frame, show="*")
    reg_password.pack(fill="x")

    def register_user():
        username = reg_username.get()
        password = reg_password.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required", parent=register_window)
            return

        if database.register_user(username, password):
            messagebox.showinfo("Success", "Account created successfully", parent=register_window)
            register_window.destroy()
        else:
            messagebox.showerror("Error", "Username already exists", parent=register_window)

    ttk.Button(frame, text="Register", command=register_user).pack(pady=15, fill="x")


# ---------- Profile Window ----------
def open_profile_window(username):
    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")
    profile_window.resizable(False, False)
    center_window(profile_window, 360, 220)

    frame = ttk.Frame(profile_window, padding=20)
    frame.pack(expand=True, fill="both")

    ttk.Label(frame, text="User Profile", font=("Arial", 14, "bold")).pack(pady=10)

    ttk.Label(frame, text=f"Username: {username}", font=("Arial", 12)).pack(pady=10)


# ---------- Dashboard Window ----------
def open_dashboard(username):
    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.resizable(False, False)
    center_window(dashboard, 360, 300)

    frame = ttk.Frame(dashboard, padding=20)
    frame.pack(expand=True, fill="both")

    ttk.Label(frame, text=f"Welcome, {username}", font=("Arial", 14, "bold")).pack(pady=10)

    def delete_account():
        confirm = messagebox.askyesno(
            "Confirm Deletion",
            "Are you sure you want to delete this account?\nThis cannot be undone."
        )

        if confirm:
            if database.delete_user(username, entry_password.get()):
                messagebox.showinfo("Deleted", "Account deleted successfully")
                dashboard.destroy()
            else:
                messagebox.showerror("Error", "Unable to delete account")

    def logout():
        dashboard.destroy()
        messagebox.showinfo("Logged out", "You have been logged out")

    ttk.Button(frame, text="Profile", command=lambda: open_profile_window(username)).pack(pady=8, fill="x")
    ttk.Button(frame, text="Delete Account", command=delete_account).pack(pady=8, fill="x")
    ttk.Button(frame, text="Logout", command=logout).pack(pady=8, fill="x")


# ---------- Login ----------
def login():
    username = entry_username.get()
    password = entry_password.get()

    if database.login_user(username, password):
        messagebox.showinfo("Welcome", f"Welcome, {username}")
        open_dashboard(username)
    else:
        messagebox.showerror("Error", "Invalid username or password")


# ---------- Main Window ----------
root = tk.Tk()
root.title("Login System")
root.resizable(False, False)
center_window(root, 360, 320)

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True, fill="both")

ttk.Label(main_frame, text="Login", font=("Arial", 18, "bold")).pack(pady=10)

ttk.Label(main_frame, text="Username:").pack(anchor="w", pady=5)
entry_username = ttk.Entry(main_frame)
entry_username.pack(fill="x")

ttk.Label(main_frame, text="Password:").pack(anchor="w", pady=5)
entry_password = ttk.Entry(main_frame, show="*")
entry_password.pack(fill="x")

ttk.Button(main_frame, text="Login", command=login).pack(pady=10, fill="x")
ttk.Button(main_frame, text="Register", command=open_register_window).pack(pady=5, fill="x")

root.mainloop()
