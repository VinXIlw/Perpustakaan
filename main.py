import tkinter as tk
import sqlite3
from tkinter import messagebox, ttk

def database():
  conn = sqlite3.connect("perpustakaan.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS buku (
            id_buku INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            pengarang TEXT NOT NULL,
            penerbit TEXT NOT NULL,
            kategori TEXT NOT NULL,
            stok INTEGER NOT NULL
        )
    """)

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS anggota (
            id_anggota INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            no_hp TEXT NOT NULL,
            alamat TEXT NOT NULL
        )
    """)

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS peminjaman (
            id_transaksi INTEGER PRIMARY KEY AUTOINCREMENT,
            id_anggota INTEGER NOT NULL,
            id_buku INTEGER NOT NULL,
            tgl_pinjam TEXT NOT NULL,
            tgl_kembali TEXT NOT NULL,
            jumlah INTEGER NOT NULL,
            status TEXT DEFAULT 'Dipinjam',
            FOREIGN KEY (id_anggota) REFERENCES anggota (id_anggota),
            FOREIGN KEY (id_buku) REFERENCES buku (id_buku)
        )
    """)

  conn.commit()
  conn.close()


root = tk.Tk()
root.title("Aplikasi Perpustakaan")
root.geometry("800x500")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)


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

root.mainloop()