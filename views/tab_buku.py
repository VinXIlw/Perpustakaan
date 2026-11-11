import tkinter as tk
from tkinter import ttk

def buat_tab_buku(notebook):
    tab_buku = ttk.Frame(notebook)
    notebook.add(tab_buku, text="Data Buku")

    tk.Label(tab_buku, text="Judul Buku:").pack(anchor="w", padx=10, pady=5)
    entry_judul = tk.Entry(tab_buku, width=35)
    entry_judul.pack(anchor="w", padx=10)

    tabel_buku = ttk.Treeview(tab_buku, columns=("ID", "Judul", "Stok"), show="headings")
    tabel_buku.heading("ID", text="ID")
    tabel_buku.heading("Judul", text="Judul")
    tabel_buku.heading("Stok", text="Stok")
    tabel_buku.pack(fill="both", expand=True, padx=10, pady=10)

    return tab_buku