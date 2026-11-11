import sqlite3

def inisialisasi_db():
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