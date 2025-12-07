from datetime import datetime
import uuid  # untuk kode transaksi unik

akun = []
donasi = [
    {"nama": "Penyandang Disabilitas - Bantuan Kursi Roda", "target": 10000000, "terkumpul": 0,
     "tanggal_mulai": "01-12-2025", "tanggal_selesai": "10-12-2025"},
    {"nama": "Penyandang Disabilitas - Bantuan Alat Bantu Dengar", "target": 12000000, "terkumpul": 0,
     "tanggal_mulai": "01-12-2025", "tanggal_selesai": "15-12-2025"},
    {"nama": "Panti Asuhan - Biaya Pendidikan", "target": 15000000, "terkumpul": 0,
     "tanggal_mulai": "01-12-2025", "tanggal_selesai": "20-12-2025"},
]
riwayat = []

akun.append({"email": "admin@gmail.com", "password": "admin123", "role": "admin"})

def daftar():
    while True:
        print("\n=== Daftar Akun Baru ===")
        print("0. Kembali")
        email = input("Email: ")
        if email == "0": return

        domain_valid = ("@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com")
        if not email.endswith(domain_valid):
            print("Email harus berakhiran domain yang valid!")
            continue

        if any(a["email"] == email for a in akun):
            print("Email sudah terdaftar!")
            continue

        password = input("Password (minimal 8 karakter / 0 untuk kembali): ")
        if password == "0": return
        if len(password) < 8:
            print("Password harus minimal 8 karakter!")
            continue

        akun.append({"email": email, "password": password, "role": "user"})
        print("Akun berhasil dibuat!")
        break

def login():
    print("\n=== Login ===")
    print("0. Kembali")
    email = input("Email: ")
    if email == "0": return None

    password = input("Password: ")
    if password == "0": return None
    if len(password) < 8:
        print("Password minimal 8 karakter!")
        return None

    for a in akun:
        if a["email"] == email and a["password"] == password:
            print("Login Berhasil!")
            return a

    print("Email atau password salah")
    return None

def tampil_donasi():
    print("\n=== DAFTAR PROGRAM DONASI ===")
    if not donasi:
        print("Belum ada donasi tersedia")
        return
    for i, d in enumerate(donasi):
        print(f"{i+1}. {d['nama']} | Target: Rp{d['target']} | Terkumpul: Rp{d['terkumpul']} | "
              f"Mulai: {d.get('tanggal_mulai','-')} | Selesai: {d.get('tanggal_selesai','-')}")

def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Daftar Pengguna")
        print("2. Tampilkan Daftar Donasi")
        print("3. Lihat Laporan Donasi")
        print("0. Kembali")
        pilih = input("Pilih: ")
        if pilih == "0": break

        if pilih == "1":
            while True:
                print("\n=== DAFTAR PENGGUNA ===")
                users = [a for a in akun if a["role"] == "user"]
                if not users:
                    print("Belum ada pengguna")
                    break
                for i, u in enumerate(users):
                    print(f"{i+1}. {u['email']}")
                print("0. Kembali")
                h = input("Pilih pengguna untuk dihapus: ")
                if h == "0": break
                if not h.isdigit(): print("Input harus angka!"); continue
                h = int(h)
                if 1 <= h <= len(users):
                    konfirmasi = input(f"Apakah Anda yakin ingin menghapus pengguna '{users[h-1]['email']}'? (y/n): ")
                    if konfirmasi.lower() == "y":
                        akun.remove(users[h-1])
                        print("Pengguna berhasil dihapus.")
                    else:
                        print("Hapus pengguna dibatalkan")
                else:
                    print("Pilihan tidak valid")

        elif pilih == "2":
            while True:
                tampil_donasi()
                print("\n1. Tambah Donasi\n2. Hapus Donasi\n3. Edit Donasi\n0. Kembali")
                a = input("Pilih: ")
                if a == "0": break

                if a == "1":
                    print("\n=== Tambah Donasi Baru ===")
                    nama = input("Nama donasi (0 batal): ")
                    if nama == "0": continue

                    target = input("Target donasi: ")
                    if target == "0": continue
                    if not target.isdigit(): print("Target harus angka!"); continue

                    tanggal_mulai = datetime.now().strftime("%d-%m-%Y")
                    tanggal_selesai = input("Tanggal selesai donasi (dd-mm-yyyy): ")
                    try:
                        datetime.strptime(tanggal_selesai, "%d-%m-%Y")
                    except:
                        print("Format tanggal salah! Harus dd-mm-yyyy")
                        continue

                    donasi.append({
                        "nama": nama,
                        "target": int(target),
                        "terkumpul": 0,
                        "tanggal_mulai": tanggal_mulai,
                        "tanggal_selesai": tanggal_selesai
                    })
                    print(f"Donasi '{nama}' berhasil ditambahkan!")

                elif a == "2":
                    h = input("Nomor donasi yang akan dihapus (0 batal): ")
                    if h == "0": continue
                    if not h.isdigit(): print("Input salah!"); continue
                    h = int(h) - 1
                    if 0 <= h < len(donasi):
                        konfirmasi = input(f"Apakah Anda yakin ingin menghapus donasi '{donasi[h]['nama']}'? (y/n): ")
                        if konfirmasi.lower() == "y":
                            del donasi[h]
                            print("Donasi berhasil dihapus")
                        else:
                            print("Hapus donasi dibatalkan")
                    else:
                        print("Pilihan tidak valid")

                elif a == "3":
                    e = input("Nomor donasi yang akan diedit (0 batal): ")
                    if e == "0": continue
                    if not e.isdigit(): print("Input salah!"); continue
                    e = int(e) - 1
                    if 0 <= e < len(donasi):
                        nama_baru = input("Nama donasi baru (0 batal): ")
                        if nama_baru == "0": continue
                        donasi[e]["nama"] = nama_baru
                        target = input("Target baru (0 batal): ")
                        if target == "0": continue
                        if not target.isdigit(): print("Target harus angka!"); continue
                        donasi[e]["target"] = int(target)

                        tanggal_selesai = input("Tanggal selesai baru (dd-mm-yyyy): ")
                        try:
                            datetime.strptime(tanggal_selesai, "%d-%m-%Y")
                            donasi[e]["tanggal_selesai"] = tanggal_selesai
                        except:
                            print("Format tanggal salah! Tetap menggunakan tanggal sebelumnya.")

                        print("Donasi berhasil diedit")
                    else:
                        print("Pilihan tidak valid")

        elif pilih == "3":
            while True:
                print("\n=== LAPORAN DONASI ===")
                if not riwayat:
                    print("Belum ada donasi")
                    break
                for i, r in enumerate(riwayat):
                    print(f"{i+1}. {r['kode_transaksi']} | {r['nama']} | {r['donasi']} | Rp{r['jumlah']} | "
                          f"{r['bank']} | {r['status']}")
                print("0. Kembali")
                h = input("Hapus laporan nomor berapa? ")
                if h == "0": break
                if not h.isdigit(): print("Input harus angka!"); continue
                h = int(h)
                if 1 <= h <= len(riwayat):
                    konfirmasi = input(f"Apakah Anda yakin ingin menghapus laporan '{riwayat[h-1]['kode_transaksi']}'? (y/n): ")
                    if konfirmasi.lower() == "y":
                        del riwayat[h-1]
                        print("Laporan berhasil dihapus")
                    else:
                        print("Hapus laporan dibatalkan")
                else:
                    print("Pilihan tidak valid")

def menu_user(pengguna):
    while True:
        print("\n=== MENU USER ===")
        print("1. Lihat Donasi")
        print("2. Berdonasi")
        print("3. History Donasi & Cetak Struk")
        print("0. Kembali")
        pilih = input("Pilih: ")
        if pilih == "0": break

        if pilih == "1":
            tampil_donasi()

        elif pilih == "2":
            tampil_donasi()
            print("0. Kembali")
            pilih_d = input("Pilih donasi: ")
            if pilih_d == "0": continue
            if not pilih_d.isdigit(): print("Input harus angka!"); continue
            pilih_d = int(pilih_d) - 1

            if not (0 <= pilih_d < len(donasi)):
                print("Pilihan tidak valid")
                continue

            d = donasi[pilih_d]

            hari_ini = datetime.now()
            tanggal_selesai = datetime.strptime(d['tanggal_selesai'], "%d-%m-%Y")
            if hari_ini > tanggal_selesai:
                print("Donasi ini sudah berakhir! Silakan pilih donasi lain.")
                continue

            if d["terkumpul"] >= d["target"]:
                print("Donasi sudah terpenuhi! Silakan pilih donasi lain.")
                continue

            nama_pendonasi = input("Nama pendonasi (0 untuk batal): ")
            if nama_pendonasi == "0": continue

            no_wa = input("Nomor WA (10-12 digit / 0 untuk batal): ")
            if no_wa == "0": continue
            if not (no_wa.isdigit() and 10 <= len(no_wa) <= 12):
                print("Nomor WA tidak valid")
                continue

            jumlah = input("Jumlah donasi (0 batal): ")
            if jumlah == "0": continue
            if not jumlah.isdigit(): print("Jumlah harus angka"); continue
            jumlah = int(jumlah)
            if jumlah < 10000:
                print("Minimal donasi 10.000")
                continue

            print("\n=== METODE PEMBAYARAN === (0 untuk batal)")
            bank_list = ["BCA", "BRI", "BTN", "Gopay", "OVO", "Dana"]
            for i, b in enumerate(bank_list):
                print(f"{i+1}. {b}")
            b = input("Pilih pembayaran: ")
            if b == "0": continue
            if not b.isdigit() or not (1 <= int(b) <= len(bank_list)):
                print("Pilihan tidak valid")
                continue

            bank = bank_list[int(b)-1]

            # --- BAGIAN PEMBAYARAN BARU (FINAL) ---
            rekening_bca = "1234567890"
            rekening_bri = "987654321001234"
            rekening_btn = "000123456789"
            nomor_wallet = "087845679677"

            if bank == "BCA":
                rekening = rekening_bca
                print(f"\nSilakan transfer ke rekening BCA: {rekening}")

            elif bank == "BRI":
                rekening = rekening_bri
                print(f"\nSilakan transfer ke rekening BRI: {rekening}")

            elif bank == "BTN":
                rekening = rekening_btn
                print(f"\nSilakan transfer ke rekening BTN: {rekening}")

            else:
                rekening = nomor_wallet
                print(f"\nSilakan transfer ke nomor {bank}: {rekening}")

            print("\nPembayaran selesai!")
            # --------------------------------------

            d["terkumpul"] += jumlah
            status = "Selesai"
            kode_transaksi = str(uuid.uuid4())[:4].upper()

            riwayat.append({
                "kode_transaksi": kode_transaksi,
                "email": pengguna["email"],
                "donasi": d["nama"],
                "nama": nama_pendonasi,
                "jumlah": jumlah,
                "bank": bank,
                "rekening": rekening,
                "status": status,
                "waktu_transaksi": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                "waktu_selesai": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            })

            print("\n===== STRUK DONASI =====")
            print(f"Kode Transaksi : {kode_transaksi}")
            print(f"Nama Pendonasi : {nama_pendonasi}")
            print(f"Donasi Program : {d['nama']}")
            print(f"Jumlah Donasi  : Rp{jumlah}")
            print(f"Bank           : {bank}")
            print(f"Waktu          : {riwayat[-1]['waktu_selesai']}")
            print("Status         : Selesai")

        elif pilih == "3":
            while True:
                print("\n=== HISTORY DONASI ===")
                data = [r for r in riwayat if r["email"] == pengguna["email"]]
                if not data:
                    print("Belum ada history")
                    break
                for i, h in enumerate(data):
                    print(f"{i+1}. {h['kode_transaksi']} | {h['donasi']} | Rp{h['jumlah']} | {h['status']} | {h['waktu_selesai']}")
                print("0. Kembali")
                c = input("Cetak struk nomor berapa? ")
                if c == "0": break
                if not c.isdigit(): print("Input harus angka!"); continue
                c = int(c)
                if 1 <= c <= len(data):
                    h = data[c-1]
                    print("\n===== STRUK DONASI =====")
                    print(f"Kode Transaksi : {h['kode_transaksi']}")
                    print(f"Nama Pendonasi : {h['nama']}")
                    print(f"Donasi Program : {h['donasi']}")
                    print(f"Jumlah Donasi  : Rp{h['jumlah']}")
                    print(f"Bank Pembayaran: {h['bank']}")
                    print(f"Rekening       : {h['rekening']}")
                    print(f"Waktu          : {h['waktu_selesai']}")
                    print(f"Status         : {h['status']}")
                    print("============================")
                else:
                    print("Pilihan tidak valid")

# PROGRAM UTAMA
while True:
    print("\n=== SISTEM DONASI ===")
    print("1. Login")
    print("2. Daftar Akun")
    print("3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        pengguna = login()
        if pengguna:
            if pengguna["role"] == "admin":
                menu_admin()
            else:
                menu_user(pengguna)

    elif pilih == "2":
        daftar()

    elif pilih == "3":
        print("Terima kasih telah menggunakan sistem donasi.")
        break

    else:
        print("Pilihan tidak valid!")