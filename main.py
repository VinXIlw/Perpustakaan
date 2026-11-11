from datetime import date
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================
# INISISALISASI DATABASE (PROGRESS 1)
# ==========================================
def buat_database():
  conn = sqlite3.connect("perpustakaan.db")
  cursor = conn.cursor()

  # Tabel Buku
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

  # Tabel Anggota
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS anggota (
            id_anggota INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            no_hp TEXT NOT NULL,
            alamat TEXT NOT NULL
        )
    """)

  # Tabel Peminjaman
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
root.title("Aplikasi Perpustakaan - Progress 1")
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

btn_frame_buku = ttk.Frame(frame_buku)
btn_frame_buku.pack(fill="x", padx=10, pady=5)
ttk.Button(btn_frame_buku, text="Tambah", command="").pack(
    side="left", padx=2
)
ttk.Button(btn_frame_buku, text="Update", command="").pack(
    side="left", padx=2
)
ttk.Button(btn_frame_buku, text="Hapus", command="").pack(
    side="left", padx=2
)

cols_buku = ("ID", "Judul", "Pengarang", "Penerbit", "Kategori", "Stok")
tabel_buku = ttk.Treeview(frame_buku, columns=cols_buku, show="headings")
for c in cols_buku:
  tabel_buku.heading(c, text=c)
  tabel_buku.column(c, width=120)
tabel_buku.pack(fill="both", expand=True, padx=10, pady=5)

frame_agt = ttk.Frame(notebook)
notebook.add(frame_agt, text="Data Anggota ")

form_agt = ttk.LabelFrame(frame_agt, text=" Form Input Anggota ")
form_agt.pack(fill="x", padx=10, pady=5)

ttk.Label(form_agt, text="Nama Anggota:").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)
entry_nama = ttk.Entry(form_agt, width=25)
entry_nama.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form_agt, text="No HP / WA:").grid(
    row=0, column=2, padx=5, pady=5, sticky="w"
)
entry_hp = ttk.Entry(form_agt, width=25)
entry_hp.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(form_agt, text="Alamat:").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
entry_alamat = ttk.Entry(form_agt, width=25)
entry_alamat.grid(row=1, column=1, padx=5, pady=5)

btn_frame_agt = ttk.Frame(frame_agt)
btn_frame_agt.pack(fill="x", padx=10, pady=5)
ttk.Button(btn_frame_agt, text="Tambah", command="").pack(
    side="left", padx=2
)
ttk.Button(btn_frame_agt, text="Update", command="").pack(
    side="left", padx=2
)
ttk.Button(btn_frame_agt, text="Hapus", command="").pack(
    side="left", padx=2
)

cols_agt = ("ID", "Nama", "No HP", "Alamat")
tabel_anggota = ttk.Treeview(frame_agt, columns=cols_agt, show="headings")
for c in cols_agt:
  tabel_anggota.heading(c, text=c)
  tabel_anggota.column(c, width=150)
tabel_anggota.pack(fill="both", expand=True, padx=10, pady=5)


frame_Transaksi = ttk.Frame(notebook)
notebook.add(frame_Transaksi, text="Transaksi Peminjaman ")

form_Transaksi = ttk.LabelFrame(frame_Transaksi, text=" Form Transaksi ")
form_Transaksi.pack(fill="x", padx=10, pady=5)

ttk.Label(form_Transaksi, text="Pilih Anggota:").grid(
    row=0, column=0, padx=5, pady=5, sticky="w"
)
cb_anggota = ttk.Combobox(form_Transaksi, width=25, state="readonly")
cb_anggota.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form_Transaksi, text="Pilih Buku:").grid(
    row=0, column=2, padx=5, pady=5, sticky="w"
)
cb_buku = ttk.Combobox(form_Transaksi, width=25, state="readonly")
cb_buku.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(form_Transaksi, text="Tgl Pinjam:").grid(
    row=1, column=0, padx=5, pady=5, sticky="w"
)
entry_tgl = ttk.Entry(form_Transaksi, width=27)
entry_tgl.insert(0, date.today().strftime("%Y-%m-%d"))
entry_tgl.grid(row=1, column=1, padx=5, pady=5)

btn_frame_Transaksi = ttk.Frame(frame_Transaksi)
btn_frame_Transaksi.pack(fill="x", padx=10, pady=5)
ttk.Button(btn_frame_Transaksi, text="Proses Pinjam", command="").pack(
    side="left", padx=2
)

cols_Transaksi = (
    "ID Transaksi",
    "Nama Anggota",
    "Judul Buku",
    "Tgl Pinjam",
    "Tgl Kembali",
    "Jumlah",
    "Status",
)
tabel_pinjam = ttk.Treeview(frame_Transaksi, columns=cols_Transaksi, show="headings")
for c in cols_Transaksi:
  tabel_pinjam.heading(c, text=c)
  tabel_pinjam.column(c, width=100)
tabel_pinjam.pack(fill="both", expand=True, padx=10, pady=5)

root.mainloop()