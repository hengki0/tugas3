# Membuat kamus berisi biodata mahasiswa dan nilai matakuliah
mahasiswa = {
    "hengki irawan": {
        "nim": "TI9220010",
        "alamat": "praya",
        "prodi": "teknik informatika",
        "semester": 2,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "Pemrograman Dasar": 92,
            "Kalkulus": 88,
            "Fisika Dasar": 90
        }
    },
    "irawan jayadi": {
        "nim": "TI19220018",
        "alamat": "janapria",
        "prodi": "tenik informatika",
        "semester": 2,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "Pemrograman Lanjut": 90,
            "Algoritma dan Struktur Data": 87,
            "Basis Data": 92
        }
    },
    "herman": {
        "nim": "SI19220009",
        "alamat": "muncan",
        "prodi": "Sistem informasi",
        "semester": 2,
        "ipk": 3.6,
        "nilai_matakuliah": {
            "Jaringan Komputer": 85,
            "Sistem Digital": 80,
            "Manajemen Basis Data": 90
        }
    },
    "wahyu": {
        "nim": "TI19220026",
        "alamat": "praya",
        "prodi": "Teknik Informatika",
        "semester": 2,
        "ipk": 3.7,
        "nilai_matakuliah": {
            "Kimia Fisika": 88,
            "Rekayasa Proses Kimia": 85,
            "Termokimia": 92
        }
    },
    "yusron": {
        "nim": "SI19220005",
        "alamat": "darmaji",
        "prodi": "sistem informasi",
        "semester": 2,
        "ipk": 3.7,
        "nilai_matakuliah": {
            "Jaringan Komputer": 80,
            "Aljabar Linier": 80,
            "Konstruksi Beton": 90
        }
    }
}

# Menampilkan biodata mahasiswa dan nilai akumulasi tiga matakuliah
for nama, data in mahasiswa.items():
    print("Biodata Mahasiswa")
    print("Nama          :", nama)
    print("NIM           :", data["nim"])
    print("Alamat        :", data["alamat"])
    print("Program Studi :", data["prodi"])
    print("Semester      :", data["semester"])
    print("IPK           :", data["ipk"])
    print("Nilai Akumulasi Matakuliah:")
    total_nilai = 0
    for matakuliah, nilai in data["nilai_matakuliah"].items():
        print("-", matakuliah, ":", nilai)
        total_nilai += nilai
    print("Total Nilai:", total_nilai)
    print("")
