print("==========Penentuan Kelulusan Siswa==========")
nama = input("masukkan nama siswa  : ")
nilai = float(input("masukkan nilai siswa : "))
lulus = nilai >= 80 
if lulus:
    print("Nama     :",nama)
    print("status   :Lulus")
else :
    print("nama     :",nama)
    print("status   :Tidak Lulus")