class mhs():
    def __init__(self,nama,nim,umur,jenis_kelamin):
        self.nama = nama
        self.nim = nim
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin
        print('(Nama mhs : {})'.format(self.nama))
    
    def tell(self):
        print('Nama: "{}" NIM:"{}"'.format(self.nama,self.nim), end=" ")

class smr(mhs):
    def __init__(self,nama,nim,matkul,kelas):
        mhs.__init__(self,nama,nim,matkul,kelas)
        self.matkul = matkul
        self.kelas = kelas
        print('(Mengambil matkul : {})'.format(self.matkul))
    
    def tell(self):
        mhs.tell(self)
        print('Matkul : "{}"'.format(self.matkul))
        print('Kelas : "{}"'.format(self.kelas))

mhsw = mhs('Sekar',1700016091,17,'p')
sm = smr('cinkus',1700016127,'forensik digital','A')

print()

total = [mhsw,sm]
for anggota in total:
    anggota.tell()