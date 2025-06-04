import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random
import time
import threading
from PIL import Image, ImageTk  # pip install pillow

# --- FAKE DDOS SIMULACIJA (EDUKATIVNA) ---
def run_ddos(ip, log_box):
    log_box.delete(1.0, tk.END)
    log_box.insert(tk.END, "Connecting to botnet")
    for _ in range(10):
        log_box.insert(tk.END, ".")
        log_box.update()
        time.sleep(0.2)
    log_box.insert(tk.END, " connected!\n")

    log_box.insert(tk.END, f"\nPokrećem simulaciju napada na {ip}...\n\n")
    log_box.update()

    for i in range(1, 101):
        log_box.insert(tk.END, f"[{i}/100] Simulirani ping ka {ip}\n")
        log_box.see(tk.END)
        log_box.update()
        time.sleep(0.05)

    log_box.insert(tk.END, "\nSimulacija završena.\n")

# --- LOGIN PROZOR ---
class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("fsociety login")
        self.frame = ttk.Frame(master, padding=20)
        self.frame.pack(expand=True)

        ttk.Label(self.frame, text="Username:").pack()
        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.pack()

        ttk.Label(self.frame, text="Password:").pack()
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.pack()

        ttk.Button(self.frame, text="Login", command=self.login).pack(pady=10)

    def login(self):
        user = self.username_entry.get()
        pw = self.password_entry.get()
        if user == "admin" and pw == "admin":
            self.frame.destroy()
            DashboardWindow(self.master)
        else:
            messagebox.showerror("Greška", "Pogrešan username ili lozinka.")

    def connection (self):
        connect localhost = to (botnet)
        define(botnet):
        1 = 91.218.67.102
        2 = 12.541.21.512
# --- DASHBOARD PROZOR ---
class DashboardWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("fsociety dashboard")

        self.frame = ttk.Frame(master, padding=10)
        self.frame.pack(fill=BOTH, expand=True)

        # Logo
        try:
            image = Image.open("daca.png")
            image = image.resize((120, 160))
            self.logo_img = ImageTk.PhotoImage(image)
            ttk.Label(self.frame, image=self.logo_img).pack(pady=5)
        except Exception as e:
            ttk.Label(self.frame, text="(Logo nije pronađen)", foreground="red").pack()

        # Header
        ttk.Label(self.frame, text="fsociety dashboard", font=("Consolas", 20, "bold")).pack(pady=10)

        # Dugmići
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack()

        ttk.Button(btn_frame, text="DOS", bootstyle=SECONDARY, command=self.not_implemented).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="DDOS", bootstyle=DANGER, command=self.show_ddos).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text="Discord Scrapper", command=self.not_implemented).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="TikTok Info Scrapper", command=self.not_implemented).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(btn_frame, text="TikTok Boost", command=self.not_implemented).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(btn_frame, text="Logout", bootstyle=WARNING, command=self.logout).grid(row=2, column=1, padx=5, pady=5)

    def not_implemented(self):
        messagebox.showinfo("Info", "Ova funkcija još nije implementirana.")

    def logout(self):
        self.frame.destroy()
        LoginWindow(self.master)

    def show_ddos(self):
        self.ddos_win = tk.Toplevel(self.master)
        self.ddos_win.title("DDOS Simulator")

        ttk.Label(self.ddos_win, text="Unesi IP adresu za simulaciju:").pack(pady=5)
        self.ip_entry = ttk.Entry(self.ddos_win)
        self.ip_entry.pack(pady=5)

        self.log_box = tk.Text(self.ddos_win, height=20, width=60, bg="#111", fg="#0f0")
        self.log_box.pack(pady=10)

        ttk.Button(self.ddos_win, text="POKRENI", bootstyle=DANGER, command=self.start_ddos_thread).pack()

    def start_ddos_thread(self):
        ip = self.ip_entry.get()
        if ip:
            threading.Thread(target=run_ddos, args=(ip, self.log_box), daemon=True).start()
        else:
            messagebox.showerror("Greška", "Unesi validnu IP adresu.")

# --- POKRETANJE APLIKACIJE ---
if __name__ == "__main__":
    app = ttk.Window(themename="darkly")
    app.geometry("600x500")
    LoginWindow(app)
    app.mainloop()
