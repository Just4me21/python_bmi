class Siswa:
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat= berat

    def hitung_bmi(self):
        tinggi_m = self.tinggi / 100
        return self.berat / (tinggi_m ** 2)

    def kategori_bmi(self):
        bmi = self.hitung_bmi()
        if bmi < 17:
            return "Kurus"
        elif 17 <= bmi <= 25:
            return "Normal"
        elif 25 < bmi <= 30:
            return "Gemuk"
        else:
            return "Obesitas"


siswa1 = Siswa("alucard", 170, 60)
siswa2 = Siswa("balmond", 160, 55)
siswa3 = Siswa("minotur", 180, 80)
siswa4 = Siswa("badang", 130,50)
siswa5 = Siswa("vexana",170, 90)


print(f"Mahasiswa dengan nama {siswa1.nama} dengan tinggi {siswa1.tinggi} cm dan berat {siswa1.berat} kg ({siswa1.kategori_bmi()})")
print(f"Mahasiswa dengan nama {siswa2.nama} dengan tinggi {siswa2.tinggi} cm dan berat {siswa2.berat} kg ({siswa2.kategori_bmi()})")
print(f"Mahasiswa dengan nama {siswa3.nama} dengan tinggi {siswa3.tinggi} cm dan berat {siswa3.berat} kg ({siswa3.kategori_bmi()})")
print(f"Mahasiswa dengan nama {siswa4.nama} dengan tinggi {siswa4.tinggi} cm dan berat {siswa4.berat} kg ({siswa4.kategori_bmi()})")
print(f"Mahasiswa dengan nama {siswa5.nama} dengan tinggi {siswa5.tinggi} cm dan berat {siswa5.berat} kg ({siswa5.kategori_bmi()})")
