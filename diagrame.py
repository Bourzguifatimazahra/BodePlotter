import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import bessel, bode, butter
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from fpdf import FPDF

def create_database():
    conn = sqlite3.connect("filters.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS filter_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filter_order INTEGER,
            cutoff REAL,
            filter_type TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(filter_order, cutoff, filter_type):
    conn = sqlite3.connect("filters.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO filter_data (filter_order, cutoff, filter_type) VALUES (?, ?, ?)",
                   (filter_order, cutoff, filter_type))
    conn.commit()
    conn.close()

def plot_bode():
    try:
        filter_order = int(order_entry.get())
        cutoff = float(cutoff_entry.get())
        filter_type = filter_var.get()

        if filter_order <= 0 or cutoff <= 0:
            raise ValueError("L'ordre et la fréquence doivent être positifs.")

        try:
            if filter_type == "Bessel":
                b, a = bessel(filter_order, cutoff, analog=True)
            else:
                b, a = butter(filter_order, cutoff, analog=True)
        except RuntimeError:
            messagebox.showwarning("Avertissement", "Échec du filtre Bessel, passage au Butterworth.")
            b, a = butter(filter_order, cutoff, analog=True)

        w, mag, phase = bode((b, a))

        plt.figure(figsize=(8, 6))
        plt.subplot(2, 1, 1)
        plt.semilogx(w, mag)
        plt.title("Diagramme de Bode")
        plt.xlabel("Fréquence [rad/s]")
        plt.ylabel("Amplitude [dB]")
        plt.grid()

        plt.subplot(2, 1, 2)
        plt.semilogx(w, phase)
        plt.xlabel("Fréquence [rad/s]")
        plt.ylabel("Phase [degrés]")
        plt.grid()
        
        save_to_db(filter_order, cutoff, filter_type)

        plt.savefig("bode_plot.png")
        plt.show()
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Diagramme de Bode", ln=True, align="C")
    pdf.image("bode_plot.png", x=10, y=20, w=180)
    pdf.output("bode_plot.pdf")
    messagebox.showinfo("Succès", "PDF généré avec succès !")

def show_history():
    conn = sqlite3.connect("filters.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM filter_data")
    rows = cursor.fetchall()
    conn.close()

    history_window = tk.Toplevel(root)
    history_window.title("Historique des filtres")
    tree = ttk.Treeview(history_window, columns=("ID", "Ordre", "Fréquence", "Type"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Ordre", text="Ordre")
    tree.heading("Fréquence", text="Fréquence")
    tree.heading("Type", text="Type")
    
    for row in rows:
        tree.insert("", "end", values=row)
    
    tree.pack()

# Interface Tkinter
root = tk.Tk()
root.title("Bode Plotter")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Générer PDF", command=generate_pdf)
file_menu.add_command(label="Afficher l'historique", command=show_history)
menu_bar.add_cascade(label="Options", menu=file_menu)

tk.Label(root, text="Ordre du filtre:").pack()
order_entry = tk.Entry(root)
order_entry.pack()

tk.Label(root, text="Fréquence de coupure:").pack()
cutoff_entry = tk.Entry(root)
cutoff_entry.pack()

filter_var = tk.StringVar(value="Bessel")
tk.Radiobutton(root, text="Bessel", variable=filter_var, value="Bessel").pack()
tk.Radiobutton(root, text="Butterworth", variable=filter_var, value="Butterworth").pack()

tk.Button(root, text="Tracer Bode", command=plot_bode).pack()

create_database()
root.mainloop()
