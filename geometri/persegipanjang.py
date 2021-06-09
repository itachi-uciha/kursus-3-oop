from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        #fungsi yang dipanggil pertama kali saat objek diciptakan
        self.p = p
        self.l = l

    def info(self):
        return f'Ini adalah objek Persegi panjang dengan panjang = {self.p} dan lebar = {self.l} memiliki luas'

    def hitung_luas(self):
        return self.p * self.l
