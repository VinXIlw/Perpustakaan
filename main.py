from datetime import date
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

def buat_database():
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


buat_database()

root = tk.Tk()
root.title("Aplikasi Perpustakaan")
root.geometry("900x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

frame_buku = ttk.Frame(notebook)
notebook.add(frame_buku, text="Data Buku ")

form_buku = ttk.LabelFrame(frame_buku, text=" Form Input Buku ")
form_buku.pack(fill="x", padx=10, pady=5)

ttk.Label(form_buku, text="Judul Buku:").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)
entry_judul = ttk.Entry(form_buku, width=25)
entry_judul.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form_buku, text="Pengarang:").grid(
    row=0, column=2, padx=5, pady=5, sticky="w"
)
entry_pengarang = ttk.Entry(form_buku, width=25)
entry_pengarang.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(form_buku, text="Penerbit:").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
entry_penerbit = ttk.Entry(form_buku, width=25)
entry_penerbit.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(form_buku, text="Kategori:").grid(
    row=1, column=2, padx=5, pady=5, sticky="w"
)
entry_kategori = ttk.Entry(form_buku, width=25)
entry_kategori.grid(row=1, column=3, padx=5, pady=5)

ttk.Label(form_buku, text="Stok:").grid(
    row=2, column=0, padx=5, pady=5, sticky="w"
)
entry_stok = ttk.Entry(form_buku, width=25)
entry_stok.grid(row=2, column=1, padx=5, pady=5)


cols_buku = ("ID", "Judul", "Pengarang", "Penerbit", "Kategori", "Stok")
tabel_buku = ttk.Treeview(frame_buku, columns=cols_buku, show="headings")
for c in cols_buku:
  tabel_buku.heading(c, text=c)
  tabel_buku.column(c, width=120)
tabel_buku.pack(fill="both", expand=True, padx=10, pady=5)

frame_anggota = ttk.Frame(notebook)
notebook.add(frame_anggota, text="Data Anggota ")

form_anggota = ttk.LabelFrame(frame_anggota, text=" Form Input Anggota ")
form_anggota.pack(fill="x", padx=10, pady=5)

ttk.Label(form_anggota, text="Nama Anggota:").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)
entry_nama = ttk.Entry(form_anggota, width=25)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form_anggota, text="No HP / WA:").grid(
    row=0, column=2, padx=5, pady=5, sticky="w"
)
entry_hp = ttk.Entry(form_anggota, width=25)
entry_hp.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(form_anggota, text="Alamat:").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
entry_alamat = ttk.Entry(form_anggota, width=25)
entry_alamat.grid(row=1, column=1, padx=5, pady=5)


cols_anggota = ("ID", "Nama", "No HP", "Alamat")
tabel_anggota = ttk.Treeview(frame_anggota, columns=cols_anggota, show="headings")
for c in cols_anggota:
  tabel_anggota.heading(c, text=c)
  tabel_anggota.column(c, width=150)
tabel_anggota.pack(fill="both", expand=True, padx=10, pady=5)

frame_transaksi = ttk.Frame(notebook)
notebook.add(frame_transaksi, text="Transaksi Peminjaman ")

form_transaksi = ttk.LabelFrame(frame_transaksi, text=" Form Transaksi ")
form_transaksi.pack(fill="x", padx=10, pady=5)

ttk.Label(form_transaksi, text="Pilih Anggota:").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)
cb_anggota = ttk.Combobox(form_transaksi, width=25, state="readonly")
cb_anggota.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form_transaksi, text="Pilih Buku:").grid(
    row=0, column=2, padx=5, pady=5, sticky="w"
)
cb_buku = ttk.Combobox(form_transaksi, width=25, state="readonly")
cb_buku.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(form_transaksi, text="Tgl Pinjam:").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
entry_tgl = ttk.Entry(form_transaksi, width=27)
entry_tgl.insert(0, date.today().strftime("%Y-%m-%d"))
entry_tgl.grid(row=1, column=1, padx=5, pady=5)

cols_transaksi = (
    "ID Transaksi",
    "Nama Anggota",
    "Judul Buku",
    "Tgl Pinjam",
    "Tgl Kembali",
    "Jumlah",
    "Status",
)
tabel_pinjam = ttk.Treeview(frame_transaksi, columns=cols_transaksi, show="headings")
for c in cols_transaksi:
  tabel_pinjam.heading(c, text=c)
  tabel_pinjam.column(c, width=100)
tabel_pinjam.pack(fill="both", expand=True, padx=10, pady=5)

root.mainloop()