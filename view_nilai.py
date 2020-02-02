from model.daftar_nilai_ import data

def cetak():
    print("\n|=========================================================================|")
    print("|========================= DAFTAR DATA MAHASISWA =========================|")
    print("|=========================================================================|")
    print("| NO | NAMA            | NIM              | TUGAS |  UTS |  UAS  |  AKHIR |")
    print("|=========================================================================|")
    no = 1
    for tabel in data.values():
        print("|{0:3} | {1:15} | {2:16} | {3:5} | {4:5} | {5:5} | {6:5} |"
              .format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
        no += 1
        print("|=========================================================================|")

def nyari():
    from view.input_nilai import cari
    cari()