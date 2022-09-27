print ('''
====================================
            Warung Dadang
         Makanan dan Minuman
====================================
          Menu
         Makanan
------------------------------------
| Kode |    Nama.    |    Harga    |
------------------------------------
|  AP  |  Nasi Pecel |Rp. 7.000,00 |
|  AS  |  Nasi Goreng|Rp. 10.000,00|
|  AD  |  Nasi Campur|Rp. 8.000,00 |

          Menu
         Minuman
------------------------------------
| Kode |    Nama.    |    Harga    |
------------------------------------
|  BP  |  Es Teh     |Rp. 3.000,00 |
|  BS  |  Teh Hangat |Rp. 4.000,00 |
|  BD  |  Es Jeruk   |Rp. 5.000,00 |
        ---------------------
          Selamat Menikmati
        ---------------------
''')
print("Anda mau pesan apa?\n\nJika Makanan Tekan 1\nJika Minuman Tekan 2\n\n")
opsi = int( input ("1/2 : "))
if opsi == 1 :
    kode = input("Masukan kode : ")
    n = int(input("Jumlah pesan : ") )
    if kode == "AP" :
        print (f'\nKode = {kode}\nNama Makanan = Nasi Pecel\nHarga = Rp.7.000,00\nTotal Bayar = Rp.{n*7000},00\n')
        print ('------Terima Kasih------')
    elif kode == "AS" :
        print (f'\nKode = {kode}\nNama Makanan = Nasi Goreng\nHarga = Rp.10.000,00\nTotal Bayar = Rp.{n*10.000},00\n')
        print ('------Terima Kasih------')
    elif kode == "AD" :
        print (f'\nKode = {kode}\nNama Makanan = Nasi Campur\nHarga = Rp.8.000,00\nTotal Bayar = Rp.{n*8000},00\n')
        print ('------Terima Kasih------')
else : 
    print ("Menu Tidak Tersedia")

if opsi == 2:
    kode = input("Masukan kode : ")
    n = int(input("Jumlah pesan : ") )
    if kode == "BP" :
        print(f'\nKode = {kode}\nNama Minuman = Es Teh\nHarga = Rp.3.000,00\nTotal Bayar = Rp.{n*3000},00\n')
        print ('------Terima Kasih------')
    elif kode == "BS" :
        print(f'\nKode = {kode}\nNama Minuman = Teh Hangat\nHarga = Rp.4.000,00\nTotal Bayar = Rp.{n*4000},00\n')
        print ('------Terima Kasih------')
    elif kode == "BD" :
        print(f'\nKode = {kode}\nNama Minuman = Es Jeruk\nHarga = Rp.5.000,00\nTotal Bayar = Rp.{n*5000},00\n')
        print ('------Terima Kasih------')
    else :
        print ("Menu Tidak Tersedia")
else:
    print ("Hanya ada opsi 1 atau 2")