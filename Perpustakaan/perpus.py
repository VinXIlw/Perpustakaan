from datetime import datetime, timedelta
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

selected_buku_id = None
selected_anggota_id = None
selected_transaksi_id = None

def buat_database():
    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS buku (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            pengarang TEXT NOT NULL,
            penerbit TEXT NOT NULL,
            kategori TEXT NOT NULL,
            stok INTEGER NOT NULL
        )
    """
    )


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS anggota (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            no_hp TEXT NOT NULL,
            alamat TEXT NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transaksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_anggota TEXT NOT NULL,
            judul_buku TEXT NOT NULL,
            tgl_pinjam TEXT NOT NULL,
            tgl_kembali TEXT NOT NULL,
            jumlah INTEGER NOT NULL,
            status TEXT NOT NULL
        )
    """
    )

    conn.commit()
    conn.close()

def muat_data_buku():
    for row in tabel_buku.get_children():
        tabel_buku.delete(row)
    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM buku")
    for row in cursor.fetchall():
        tabel_buku.insert("", tk.END, values=row)
    conn.close()
    update_dropdown_peminjaman()


def tambah_buku():
    judul, pengarang, penerbit, kategori, stok = (
        entry_judul.get(),
        entry_pengarang.get(),
        entry_penerbit.get(),
        entry_kategori.get(),
        entry_stok.get(),
    )
    if not all([judul, pengarang, penerbit, kategori, stok]):
        messagebox.showerror("Error", "Semua kolom form buku wajib diisi!")
        return
    try:
        conn = sqlite3.connect("perpustakaan.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO buku (judul, pengarang, penerbit, kategori, stok) VALUES (?, ?, ?, ?, ?)",
            (judul, pengarang, penerbit, kategori, int(stok)),
        )
        conn.commit()
        conn.close()
        muat_data_buku()
        bersihkan_form_buku()
        messagebox.showinfo("Sukses", "Data buku berhasil ditambahkan!")
    except ValueError:
        messagebox.showerror("Error", "Stok harus berupa angka!")


def pilih_buku(event):
    global selected_buku_id
    try:
        item = tabel_buku.selection()[0]
        vals = tabel_buku.item(item, "values")
        selected_buku_id = vals[0]
        for e, v in zip(
            [entry_judul, entry_pengarang, entry_penerbit, entry_kategori, entry_stok],
            vals[1:],
        ):
            e.delete(0, tk.END)
            e.insert(0, v)
    except IndexError:
        pass


def update_buku():
    global selected_buku_id
    if not selected_buku_id:
        messagebox.showerror("Error", "Pilih data buku terlebih dahulu!")
        return
    judul, pengarang, penerbit, kategori, stok = (
        entry_judul.get(),
        entry_pengarang.get(),
        entry_penerbit.get(),
        entry_kategori.get(),
        entry_stok.get(),
    )
    try:
        conn = sqlite3.connect("perpustakaan.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE buku SET judul=?, pengarang=?, penerbit=?, kategori=?, stok=? WHERE id=?",
            (judul, pengarang, penerbit, kategori, int(stok), selected_buku_id),
        )
        conn.commit()
        conn.close()
        muat_data_buku()
        bersihkan_form_buku()
        messagebox.showinfo("Sukses", "Data buku diperbarui!")
    except ValueError:
        messagebox.showerror("Error", "Stok harus berupa angka!")


def hapus_buku():
    global selected_buku_id
    if not selected_buku_id:
        messagebox.showerror("Error", "Pilih data buku yang akan dihapus!")
        return
    if messagebox.askyesno(
        "Konfirmasi", "Yakin ingin menghapus buku ini?"
    ):
        conn = sqlite3.connect("perpustakaan.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM buku WHERE id=?", (selected_buku_id,))
        conn.commit()
        conn.close()
        muat_data_buku()
        bersihkan_form_buku()
        messagebox.showinfo("Sukses", "Buku berhasil dihapus.")


def bersihkan_form_buku():
    global selected_buku_id
    selected_buku_id = None
    for e in [
        entry_judul,
        entry_pengarang,
        entry_penerbit,
        entry_kategori,
        entry_stok,
    ]:
        e.delete(0, tk.END)

def muat_data_anggota():
    for row in tabel_anggota.get_children():
        tabel_anggota.delete(row)
    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM anggota")
    for row in cursor.fetchall():
        tabel_anggota.insert("", tk.END, values=row)
    conn.close()
    update_dropdown_peminjaman()


def tambah_anggota():
    nama, no_hp, alamat = (
        entry_nama_agt.get(),
        entry_hp_agt.get(),
        entry_alamat_agt.get(),
    )
    if not all([nama, no_hp, alamat]):
        messagebox.showerror("Error", "Semua kolom form anggota wajib diisi!")
        return
    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO anggota (nama, no_hp, alamat) VALUES (?, ?, ?)",
        (nama, no_hp, alamat),
    )
    conn.commit()
    conn.close()
    muat_data_anggota()
    bersihkan_form_anggota()
    messagebox.showinfo("Sukses", "Anggota berhasil ditambahkan!")


def pilih_anggota(event):
    global selected_anggota_id
    try:
        item = tabel_anggota.selection()[0]
        vals = tabel_anggota.item(item, "values")
        selected_anggota_id = vals[0]
        for e, v in zip([entry_nama_agt, entry_hp_agt, entry_alamat_agt], vals[1:]):
            e.delete(0, tk.END)
            e.insert(0, v)
    except IndexError:
        pass


def update_anggota():
    global selected_anggota_id
    if not selected_anggota_id:
        messagebox.showerror("Error", "Pilih data anggota terlebih dahulu!")
        return
    nama, no_hp, alamat = (
        entry_nama_agt.get(),
        entry_hp_agt.get(),
        entry_alamat_agt.get(),
    )
    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE anggota SET nama=?, no_hp=?, alamat=? WHERE id=?",
        (nama, no_hp, alamat, selected_anggota_id),
    )
    conn.commit()
    conn.close()
    muat_data_anggota()
    bersihkan_form_anggota()
    messagebox.showinfo("Sukses", "Data anggota diperbarui!")


def hapus_anggota():
    global selected_anggota_id
    if not selected_anggota_id:
        messagebox.showerror("Error", "Pilih data anggota yang akan dihapus!")
        return
    if messagebox.askyesno(
        "Konfirmasi", "Yakin ingin menghapus anggota ini?"
    ):
        conn = sqlite3.connect("perpustakaan.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM anggota WHERE id=?", (selected_anggota_id,))
        conn.commit()
        conn.close()
        muat_data_anggota()
        bersihkan_form_anggota()
        messagebox.showinfo("Sukses", "Anggota berhasil dihapus.")


def bersihkan_form_anggota():
    global selected_anggota_id
    selected_anggota_id = None
    for e in [entry_nama_agt, entry_hp_agt, entry_alamat_agt]:
        e.delete(0, tk.END)

def update_dropdown_peminjaman():
    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nama FROM anggota")
    combo_anggota["values"] = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT judul FROM buku WHERE stok > 0")
    combo_buku["values"] = [row[0] for row in cursor.fetchall()]
    conn.close()


def muat_data_transaksi():
    for row in tabel_transaksi.get_children():
        tabel_transaksi.delete(row)
    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transaksi")
    for row in cursor.fetchall():
        tabel_transaksi.insert("", tk.END, values=row)
    conn.close()


def proses_pinjam():
    nama = combo_anggota.get()
    judul = combo_buku.get()
    tgl_pinjam = entry_tgl_pinjam.get()
    tgl_kembali = entry_tgl_kembali.get()
    jumlah = entry_jml.get()

    if not all([nama, judul, tgl_pinjam, tgl_kembali, jumlah]):
        messagebox.showerror("Error", "Semua kolom form transaksi wajib diisi!")
        return

    try:
        jml_int = int(jumlah)
        conn = sqlite3.connect("perpustakaan.db")
        cursor = conn.cursor()


        cursor.execute("SELECT stok FROM buku WHERE judul=?", (judul,))
        stok_db = cursor.fetchone()
        if not stok_db or stok_db[0] < jml_int:
            messagebox.showerror("Error", "Stok buku tidak mencukupi!")
            conn.close()
            return

        cursor.execute(
            "UPDATE buku SET stok = stok - ? WHERE judul = ?", (jml_int, judul)
        )

        cursor.execute(
            "INSERT INTO transaksi (nama_anggota, judul_buku, tgl_pinjam, tgl_kembali, jumlah, status) VALUES (?, ?, ?, ?, ?, ?)",
            (nama, judul, tgl_pinjam, tgl_kembali, jml_int, "Dipinjam"),
        )
        conn.commit()
        conn.close()

        muat_data_buku()
        muat_data_transaksi()
        messagebox.showinfo("Sukses", "Transaksi peminjaman berhasil diproses!")
    except ValueError:
        messagebox.showerror("Error", "Jumlah buku harus berupa angka!")


def pilih_transaksi(event):
    global selected_transaksi_id
    try:
        item = tabel_transaksi.selection()[0]
        vals = tabel_transaksi.item(item, "values")
        selected_transaksi_id = vals[0]
        combo_anggota.set(vals[1])
        combo_buku.set(vals[2])
        entry_tgl_pinjam.delete(0, tk.END)
        entry_tgl_pinjam.insert(0, vals[3])
        entry_tgl_kembali.delete(0, tk.END)
        entry_tgl_kembali.insert(0, vals[4])
        entry_jml.delete(0, tk.END)
        entry_jml.insert(0, vals[5])
    except IndexError:
        pass


def kembalikan_buku():
    global selected_transaksi_id
    if not selected_transaksi_id:
        messagebox.showerror("Error", "Pilih transaksi pada tabel terlebih dahulu!")
        return

    conn = sqlite3.connect("perpustakaan.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT judul_buku, jumlah, status FROM transaksi WHERE id=?",
        (selected_transaksi_id,),
    )
    res = cursor.fetchone()
    if res[2] == "Dikembalikan":
        messagebox.showwarning(
            "Peringatan", "Buku ini sudah dikembalikan sebelumnya!"
        )
        conn.close()
        return

    judul, jumlah = res[0], res[1]

    cursor.execute(
        "UPDATE buku SET stok = stok + ? WHERE judul = ?", (jumlah, judul)
    )

    cursor.execute(
        "UPDATE transaksi SET status = 'Dikembalikan' WHERE id = ?",
        (selected_transaksi_id,),
    )

    conn.commit()
    conn.close()

    muat_data_buku()
    muat_data_transaksi()
    messagebox.showinfo("Sukses", "Buku berhasil dikembalikan & stok dipulihkan!")


def hapus_transaksi():
    global selected_transaksi_id
    if not selected_transaksi_id:
        messagebox.showerror("Error", "Pilih transaksi yang akan dihapus!")
        return
    if messagebox.askyesno(
        "Konfirmasi", "Yakin ingin menghapus riwayat transaksi ini?"
    ):
        conn = sqlite3.connect("perpustakaan.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM transaksi WHERE id=?", (selected_transaksi_id,))
        conn.commit()
        conn.close()
        muat_data_transaksi()
        messagebox.showinfo("Sukses", "Riwayat transaksi dihapus.")


def bersihkan_form_transaksi():
    global selected_transaksi_id
    selected_transaksi_id = None
    combo_anggota.set("")
    combo_buku.set("")
    entry_jml.delete(0, tk.END)
    entry_jml.insert(0, "1")

buat_database()

root = tk.Tk()
root.title("Aplikasi Perpustakaan")
root.geometry("800x550")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

tab_buku = ttk.Frame(notebook)
notebook.add(tab_buku, text="Data Buku")

f_buku = tk.LabelFrame(tab_buku, text=" Form Input Buku ", padx=10, pady=10)
f_buku.pack(fill="x", padx=10, pady=10)

tk.Label(f_buku, text="Judul Buku:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_judul = tk.Entry(f_buku, width=28)
entry_judul.grid(row=0, column=1, padx=5, pady=5)

tk.Label(f_buku, text="Pengarang:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
entry_pengarang = tk.Entry(f_buku, width=28)
entry_pengarang.grid(row=0, column=3, padx=5, pady=5)

tk.Label(f_buku, text="Penerbit:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_penerbit = tk.Entry(f_buku, width=28)
entry_penerbit.grid(row=1, column=1, padx=5, pady=5)

tk.Label(f_buku, text="Kategori:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
entry_kategori = tk.Entry(f_buku, width=28)
entry_kategori.grid(row=1, column=3, padx=5, pady=5)

tk.Label(f_buku, text="Stok:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_stok = tk.Entry(f_buku, width=28)
entry_stok.grid(row=2, column=1, padx=5, pady=5)

btn_f_buku = tk.Frame(tab_buku)
btn_f_buku.pack(fill="x", padx=10, pady=5)
tk.Button(btn_f_buku, text="Tambah", width=10, command=tambah_buku).pack(
    side="left", padx=5
)
tk.Button(btn_f_buku, text="Update", width=10, command=update_buku).pack(
    side="left", padx=5
)
tk.Button(btn_f_buku, text="Hapus", width=10, command=hapus_buku).pack(
    side="left", padx=5
)
tk.Button(
    btn_f_buku, text="Bersihkan", width=10, command=bersihkan_form_buku
).pack(side="left", padx=5)

col_buku = ("ID", "Judul", "Pengarang", "Penerbit", "Kategori", "Stok")
tabel_buku = ttk.Treeview(tab_buku, columns=col_buku, show="headings", height=10)
for c, w in zip(
    col_buku, [40, 160, 130, 120, 110, 60]
):
    tabel_buku.heading(c, text=c)
    tabel_buku.column(c, width=w, anchor="center" if c in ["ID", "Stok"] else "w")
tabel_buku.pack(fill="both", expand=True, padx=10, pady=10)
tabel_buku.bind("<ButtonRelease-1>", pilih_buku)


tab_anggota = ttk.Frame(notebook)
notebook.add(tab_anggota, text="Data Anggota")

f_agt = tk.LabelFrame(tab_anggota, text=" Form Input Anggota ", padx=10, pady=10)
f_agt.pack(fill="x", padx=10, pady=10)

tk.Label(f_agt, text="Nama Anggota:").grid(
    row=0, column=0, sticky="w", padx=5, pady=5
)
entry_nama_agt = tk.Entry(f_agt, width=30)
entry_nama_agt.grid(row=0, column=1, padx=5, pady=5)

tk.Label(f_agt, text="No HP / WA:").grid(
    row=0, column=2, sticky="w", padx=5, pady=5
)
entry_hp_agt = tk.Entry(f_agt, width=30)
entry_hp_agt.grid(row=0, column=3, padx=5, pady=5)

tk.Label(f_agt, text="Alamat:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_alamat_agt = tk.Entry(f_agt, width=30)
entry_alamat_agt.grid(row=1, column=1, padx=5, pady=5)

btn_f_agt = tk.Frame(tab_anggota)
btn_f_agt.pack(fill="x", padx=10, pady=5)
tk.Button(btn_f_agt, text="Tambah", width=10, command=tambah_anggota).pack(
    side="left", padx=5
)
tk.Button(btn_f_agt, text="Update", width=10, command=update_anggota).pack(
    side="left", padx=5
)
tk.Button(btn_f_agt, text="Hapus", width=10, command=hapus_anggota).pack(
    side="left", padx=5
)
tk.Button(
    btn_f_agt, text="Bersihkan", width=10, command=bersihkan_form_anggota
).pack(side="left", padx=5)

col_agt = ("ID", "Nama", "No HP", "Alamat")
tabel_anggota = ttk.Treeview(tab_anggota, columns=col_agt, show="headings", height=10)
for c, w in zip(col_agt, [50, 200, 150, 220]):
    tabel_anggota.heading(c, text=c)
    tabel_anggota.column(c, width=w, anchor="center" if c == "ID" else "w")
tabel_anggota.pack(fill="both", expand=True, padx=10, pady=10)
tabel_anggota.bind("<ButtonRelease-1>", pilih_anggota)


tab_transaksi = ttk.Frame(notebook)
notebook.add(tab_transaksi, text="Transaksi Peminjaman")

f_trx = tk.LabelFrame(tab_transaksi, text=" Form Transaksi ", padx=10, pady=10)
f_trx.pack(fill="x", padx=10, pady=10)

tk.Label(f_trx, text="Pilih Anggota:").grid(
    row=0, column=0, sticky="w", padx=5, pady=5
)
combo_anggota = ttk.Combobox(f_trx, width=28, state="readonly")
combo_anggota.grid(row=0, column=1, padx=5, pady=5)

tk.Label(f_trx, text="Pilih Buku:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
combo_buku = ttk.Combobox(f_trx, width=28, state="readonly")
combo_buku.grid(row=0, column=3, padx=5, pady=5)

tgl_hari_ini = datetime.now().strftime("%Y-%m-%d")
tgl_depan = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

tk.Label(f_trx, text="Tanggal Pinjam:").grid(
    row=1, column=0, sticky="w", padx=5, pady=5
)
entry_tgl_pinjam = tk.Entry(f_trx, width=30)
entry_tgl_pinjam.grid(row=1, column=1, padx=5, pady=5)
entry_tgl_pinjam.insert(0, tgl_hari_ini)

tk.Label(f_trx, text="Rencana Kembali:").grid(
    row=1, column=2, sticky="w", padx=5, pady=5
)
entry_tgl_kembali = tk.Entry(f_trx, width=30)
entry_tgl_kembali.grid(row=1, column=3, padx=5, pady=5)
entry_tgl_kembali.insert(0, tgl_depan)

tk.Label(f_trx, text="Jumlah:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_jml = tk.Entry(f_trx, width=30)
entry_jml.grid(row=2, column=1, padx=5, pady=5)
entry_jml.insert(0, "1")

btn_f_trx = tk.Frame(tab_transaksi)
btn_f_trx.pack(fill="x", padx=10, pady=5)
tk.Button(
    btn_f_trx, text="Proses Pinjam", width=12, command=proses_pinjam
).pack(side="left", padx=5)
tk.Button(
    btn_f_trx, text="Kembalikan Buku", width=14, command=kembalikan_buku
).pack(side="left", padx=5)
tk.Button(
    btn_f_trx, text="Hapus Transaksi", width=13, command=hapus_transaksi
).pack(side="left", padx=5)
tk.Button(
    btn_f_trx, text="Bersihkan Form", width=12, command=bersihkan_form_transaksi
).pack(side="left", padx=5)

col_trx = (
    "ID Transaksi",
    "Nama Anggota",
    "Judul Buku",
    "Tanggal Pinjam",
    "Tanggal Kembali",
    "Jumlah",
    "Status",
)
tabel_transaksi = ttk.Treeview(
    tab_transaksi, columns=col_trx, show="headings", height=9
)
for c, w in zip(col_trx, [80, 130, 130, 100, 100, 60, 90]):
    tabel_transaksi.heading(c, text=c)
    tabel_transaksi.column(c, width=w, anchor="center" if c in ["ID Transaksi", "Jumlah", "Status"] else "w")
tabel_transaksi.pack(fill="both", expand=True, padx=10, pady=10)
tabel_transaksi.bind("<ButtonRelease-1>", pilih_transaksi)


muat_data_buku()
muat_data_anggota()
muat_data_transaksi()

root.mainloop()