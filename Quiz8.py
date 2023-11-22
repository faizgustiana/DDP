#NO1

def profil():
    print(nama, alamat, gender, umur, hoby)
    
nama = "Faiz"
alamat = "Bogor"
gender = "Laki laki"
umur = "18"
hoby = "Banyak"
profil()

#NO2
def kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    print()

#NO3
def ganjil(n):
    for i in range(1, n+2, 2):
        print(i)
ganjil(99)
