import tkinter as tk
from tkinter import ttk

def buat_tampilan(frame, fungsi_navigasi, frame_buku, frame_anggota, frame_pinjam):
    ttk.Label(frame, text="Halaman Utama (Dashboard / Menu)", font=("Arial", 14)).pack(pady=20)
    
    ttk.Button(frame, text="Menu/Form Daftar Buku", command=lambda: fungsi_navigasi(frame_buku)).pack(pady=5)
    ttk.Button(frame, text="Menu/Form Daftar Anggota", command=lambda: fungsi_navigasi(frame_anggota)).pack(pady=5)
    ttk.Button(frame, text="Form Peminjaman & Pengembalian Buku", command=lambda: fungsi_navigasi(frame_pinjam)).pack(pady=5)