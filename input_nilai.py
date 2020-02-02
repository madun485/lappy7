from model.daftar_nilai_ import tambah_data
def inputan():
    nama = input("NAMA : ")
    nim = int(input("NIM : "))
    tugas = int(input("TUGAS : "))
    uts = int(input("UTS : "))
    uas = int(input("UAS : "))
    tambah_data(nama, nim, tugas, uts, uas)

def edit():
    from model.daftar_nilai_ import edit_data
    edit_data(nama=input("Masukan nama untuk edit data : "))

def delete():
    from model.daftar_nilai_ import delete_data
    delete_data(nama=input("Masukan nama untuk menghapus data : "))

def cari():
    from model.daftar_nilai_ import cari_data
    cari_data(nama=input("Masukan nama yang di cari : "))