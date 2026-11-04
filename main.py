import tkinter as tk
from tkinter import ttk
import sqlite3
import dashboard

conn = sqlite3.connect("perpustakaan.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS buku (id INTEGER PRIMARY KEY AUTOINCREMENT, judul TEXT, pengarang TEXT, penerbit TEXT, kategori TEXT, stok INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS anggota (id INTEGER PRIMARY KEY AUTOINCREMENT, nama TEXT, hp TEXT, alamat TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS pinjam (id INTEGER PRIMARY KEY AUTOINCREMENT, nama TEXT, id_buku INTEGER, tgl_pinjam TEXT, tgl_kembali TEXT, jumlah INTEGER)")
conn.commit()
conn.close()

root = tk.Tk()
root.geometry("600x500")

frame_menu = ttk.Frame(root)
frame_buku = ttk.Frame(root)
frame_anggota = ttk.Frame(root)
frame_pinjam = ttk.Frame(root)

def buka_halaman(halaman):
    frame_menu.pack_forget()
    frame_buku.pack_forget()
    frame_anggota.pack_forget()
    frame_pinjam.pack_forget()
    
    halaman.pack(fill="both", expand=True)

dashboard.buat_tampilan(frame_menu, buka_halaman, frame_buku, frame_anggota, frame_pinjam)

buka_halaman(frame_menu)
root.mainloop()