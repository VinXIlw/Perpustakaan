import tkinter as tk
from tkinter import ttk

from database.koneksi import inisialisasi_db
from views.tab_buku import buat_tab_buku
from views.tab_anggota import buat_tab_anggota
from views.tab_transaksi import buat_tab_transaksi

def main():
    inisialisasi_db()

    root = tk.Tk()
    root.title("Aplikasi Perpustakaan")
    root.geometry("800x500")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    buat_tab_buku(notebook)
    buat_tab_anggota(notebook)
    buat_tab_transaksi(notebook)

    root.mainloop()

if __name__ == "__main__":
    main()