import tkinter as tk
from tkinter import ttk

def buat_tab_anggota(notebook):
    tab_anggota = ttk.Frame(notebook)
    notebook.add(tab_anggota, text="Data Anggota")

    tk.Label(tab_anggota, text="Nama Anggota:").pack(anchor="w", padx=10, pady=5)
    entry_nama = tk.Entry(tab_anggota, width=35)
    entry_nama.pack(anchor="w", padx=10)

    tabel_anggota = ttk.Treeview(tab_anggota, columns=("ID", "Nama", "No HP"), show="headings")
    tabel_anggota.heading("ID", text="ID")
    tabel_anggota.heading("Nama", text="Nama")
    tabel_anggota.heading("No HP", text="No HP")
    tabel_anggota.pack(fill="both", expand=True, padx=10, pady=10)

    return tab_anggota