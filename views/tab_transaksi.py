import tkinter as tk
from tkinter import ttk

def buat_tab_transaksi(notebook):
    tab_transaksi = ttk.Frame(notebook)
    notebook.add(tab_transaksi, text="Transaksi & Pengembalian")

    tk.Label(tab_transaksi, text="Pilih Anggota:").pack(anchor="w", padx=10, pady=5)
    cb_anggota = ttk.Combobox(tab_transaksi, width=33, state="readonly")
    cb_anggota.pack(anchor="w", padx=10)

    tk.Label(tab_transaksi, text="Pilih Buku:").pack(anchor="w", padx=10, pady=5)
    cb_buku = ttk.Combobox(tab_transaksi, width=33, state="readonly")
    cb_buku.pack(anchor="w", padx=10)

    tabel_transaksi = ttk.Treeview(tab_transaksi, columns=("ID", "Anggota", "Buku", "Status"), show="headings")
    tabel_transaksi.heading("ID", text="ID")
    tabel_transaksi.heading("Anggota", text="Nama Anggota")
    tabel_transaksi.heading("Buku", text="Judul Buku")
    tabel_transaksi.heading("Status", text="Status")
    tabel_transaksi.pack(fill="both", expand=True, padx=10, pady=10)

    return tab_transaksi