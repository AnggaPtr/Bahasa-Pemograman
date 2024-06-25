import bisect

def pencarian_biner_bisect(buku, tahun_target):
    i = bisect.bisect_left([buku[1] for buku in buku], tahun_target)
    if i!= len(buku) and buku[i][1] == tahun_target:
        return i
    else:
        return -1

buku = [
    ("Buku A", 1995),
    ("Buku B", 1998),
    ("Buku C", 2000),
    ("Buku D", 2002),
    ("Buku E", 2005),
    ("Buku F", 2008)
]

while True:
    tahun_target = int(input("Masukkan tahun yang ingin dicari: "))
    result = pencarian_biner_bisect(buku, tahun_target)
    if result!= -1:
        print( buku[result][0], "diterbitkan pada tahun", tahun_target)
    else:
        print("Tidak ada buku yang diterbitkan pada tahun", tahun_target)
    
    response = input("Do you want to continue? (y/n) : ")
    if response.lower()!= 'y':
        break